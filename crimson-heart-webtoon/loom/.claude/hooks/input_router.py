#!/usr/bin/env python3
"""
Input Router - Natural language routing for Writing Hub entry.

Routes user input to appropriate mode (book project vs quick session).
Uses tiered classification: fast patterns first, Claude only for ambiguity.

Usage:
    from input_router import route_input, RoutingResult

    result = route_input("vampire romance tonight")
    # result.mode == 'session', result.entry_type == 'character'

    result = route_input("continue halcyon chapter 4")
    # result.mode == 'book', result.project_name == 'halcyon-verge-universe'

Tiers:
    1. Explicit keywords (highest confidence)
    2. Chapter/scene references
    3. Known project name detection
    4. Quick session signal patterns
    5. Ambiguous (need clarification)
"""
import re
import sys
from dataclasses import dataclass
from difflib import get_close_matches
from pathlib import Path
from typing import Literal, Optional

# Add hooks directory to path for local imports
_hooks_dir = Path(__file__).resolve().parent
if str(_hooks_dir) not in sys.path:
    sys.path.insert(0, str(_hooks_dir))

from state_manager import read_state, BOOKS_DIR
from session_manager import detect_entry_type


@dataclass
class RoutingResult:
    """Result of input routing decision."""
    mode: Literal['book', 'session', 'ambiguous']
    confidence: float = 1.0

    # Book project fields
    project_name: Optional[str] = None
    chapter: Optional[str] = None

    # Quick session fields
    entry_type: Optional[str] = None
    initial_concept: Optional[str] = None

    # Ambiguous fields
    clarification: Optional[dict] = None

    # Metadata
    match_tier: int = 0
    reasoning: str = ""


# Load project names at module level for fast lookup
def _load_project_names() -> list[str]:
    """Load available project names from _books directory."""
    if not BOOKS_DIR.exists():
        return []
    return sorted([
        p.name for p in BOOKS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith('.') and not p.name.startswith('_')
    ])


PROJECT_NAMES = _load_project_names()

# Routing patterns
BOOK_KEYWORDS = ['continue', 'resume', 'back to', 'work on', 'return to']
NEW_BOOK_KEYWORDS = ['start a book', 'new book', 'write a book', 'book project', 'start a novel', 'new novel', 'write a novel']
SESSION_KEYWORDS = ['quick session', 'new session', 'tonight', 'something ']
CHAPTER_PATTERN = re.compile(r'\b(?:chapter|ch\.?|scene)\s*(\d+)', re.IGNORECASE)

# Session signal patterns for tier 4 classification
SESSION_SIGNALS = {
    'timing': [r'\btonight\b', r'\btoday\b', r'\bquick\b', r'\bshort\b'],
    'mood': [r'\bsomething\b', r'\bin the mood\b', r'\bfeel like\b'],
    'vibe': [r'\b(dark|light|fun|intense|cozy|spicy|sweet)\b'],
    'archetype': [r'\b(vampire|demon|angel|maid|butler|boss)\b'],
    'trope': [r'\b(enemies to lovers|fake dating|slow burn)\b']
}


def route_input(user_input: str) -> RoutingResult:
    """
    Route user input to appropriate mode.

    Uses tiered classification cascade:
    1. Explicit command keywords (highest confidence)
    2. Chapter/scene references
    3. Known project name detection
    4. Quick session signal patterns
    5. Ambiguous (need clarification)

    Args:
        user_input: Natural language input from user

    Returns:
        RoutingResult with mode, confidence, and relevant metadata
    """
    if not user_input or not user_input.strip():
        return RoutingResult(
            mode='ambiguous',
            clarification=_generate_empty_clarification(),
            reasoning="Empty input"
        )

    input_lower = user_input.lower().strip()

    # Tier 1: Explicit book keywords
    for kw in BOOK_KEYWORDS:
        if kw in input_lower:
            return _route_book_from_keyword(user_input, input_lower, kw)

    # Tier 1a: New book project keywords
    for kw in NEW_BOOK_KEYWORDS:
        if kw in input_lower:
            return RoutingResult(
                mode='book',
                confidence=0.9,
                project_name=None,  # No project yet - needs creation
                match_tier=1,
                reasoning=f"Matched new book keyword '{kw}'"
            )

    # Tier 1b: Explicit session keywords
    for kw in SESSION_KEYWORDS:
        if kw in input_lower:
            return _route_session(user_input, tier=1, reasoning=f"Matched session keyword '{kw}'")

    # Tier 2: Chapter/scene reference
    chapter_match = CHAPTER_PATTERN.search(input_lower)
    if chapter_match:
        return _route_book_with_chapter(user_input, input_lower, chapter_match.group(1))

    # Tier 3: Project name detection
    project_match = _find_project_in_input(user_input)
    if project_match and project_match['confidence'] >= 0.8:
        return RoutingResult(
            mode='book',
            confidence=project_match['confidence'],
            project_name=project_match['name'],
            match_tier=3,
            reasoning=f"Matched project '{project_match['name']}' ({project_match['match_type']})"
        )

    # Tier 4: Quick session signals
    entry_type = detect_entry_type(user_input)
    if entry_type in ['character', 'situation']:
        return _route_session(
            user_input,
            tier=4,
            entry_type=entry_type,
            reasoning=f"Detected {entry_type}-first entry"
        )

    if _has_strong_session_signals(input_lower):
        return _route_session(
            user_input,
            tier=4,
            entry_type=entry_type,
            reasoning="Strong session signals detected"
        )

    # Tier 5: Ambiguous - need clarification
    return RoutingResult(
        mode='ambiguous',
        confidence=0.4,
        clarification=_generate_clarification(user_input, project_match),
        match_tier=5,
        reasoning="No strong signals for either mode"
    )


def _route_book_from_keyword(user_input: str, input_lower: str, keyword: str) -> RoutingResult:
    """Route to book mode when explicit keyword detected."""
    # Check for project name after keyword
    project_match = _find_project_in_input(user_input)

    # If no explicit project, check for implicit continue (last active)
    if not project_match or project_match['confidence'] < 0.5:
        session = read_state('session.json')
        if session.get('active_project'):
            return RoutingResult(
                mode='book',
                confidence=0.9,
                project_name=session['active_project'],
                match_tier=1,
                reasoning=f"Keyword '{keyword}' + implicit continue of last project"
            )

    # Extract chapter if present
    chapter_match = CHAPTER_PATTERN.search(input_lower)
    chapter = chapter_match.group(1) if chapter_match else None

    if project_match:
        return RoutingResult(
            mode='book',
            confidence=project_match['confidence'],
            project_name=project_match['name'],
            chapter=chapter,
            match_tier=1,
            reasoning=f"Keyword '{keyword}' + project '{project_match['name']}'"
        )

    # Have keyword but no project - ambiguous, show project list
    return RoutingResult(
        mode='ambiguous',
        confidence=0.5,
        clarification=_generate_project_list_clarification(keyword),
        match_tier=1,
        reasoning=f"Keyword '{keyword}' but no project identified"
    )


def _route_book_with_chapter(user_input: str, input_lower: str, chapter: str) -> RoutingResult:
    """Route to book mode when chapter reference detected."""
    project_match = _find_project_in_input(user_input)

    if project_match:
        return RoutingResult(
            mode='book',
            confidence=0.9,
            project_name=project_match['name'],
            chapter=chapter,
            match_tier=2,
            reasoning=f"Chapter {chapter} reference + project '{project_match['name']}'"
        )

    # Check for last active project
    session = read_state('session.json')
    if session.get('active_project'):
        return RoutingResult(
            mode='book',
            confidence=0.85,
            project_name=session['active_project'],
            chapter=chapter,
            match_tier=2,
            reasoning=f"Chapter {chapter} reference + last active project"
        )

    return RoutingResult(
        mode='ambiguous',
        confidence=0.6,
        clarification=_generate_project_list_clarification(f"chapter {chapter}"),
        match_tier=2,
        reasoning=f"Chapter {chapter} reference but no project context"
    )


def _route_session(
    user_input: str,
    tier: int,
    entry_type: str = None,
    reasoning: str = ""
) -> RoutingResult:
    """Route to quick session mode."""
    if not entry_type:
        entry_type = detect_entry_type(user_input)

    return RoutingResult(
        mode='session',
        confidence=0.9 if tier <= 2 else 0.75,
        entry_type=entry_type,
        initial_concept=user_input,
        match_tier=tier,
        reasoning=reasoning
    )


def _find_project_in_input(user_input: str) -> dict | None:
    """
    Find project name in user input using multiple strategies.

    Returns dict with name, confidence, and match_type, or None.
    """
    input_lower = user_input.lower()

    # Strategy 1: Exact substring match (highest confidence)
    for project in PROJECT_NAMES:
        project_lower = project.lower().replace('-', ' ').replace('_', ' ')
        if project_lower in input_lower:
            return {'name': project, 'confidence': 1.0, 'match_type': 'exact'}

        # Check all project words present
        words = project_lower.split()
        if len(words) > 1 and all(w in input_lower for w in words):
            return {'name': project, 'confidence': 0.95, 'match_type': 'words'}

    # Strategy 2: Partial match (e.g., "halcyon" -> "halcyon-verge-universe")
    # Only match words > 3 chars to avoid false positives
    input_words = input_lower.split()
    for project in PROJECT_NAMES:
        project_lower = project.lower()
        for word in input_words:
            if len(word) >= 4:
                if word in project_lower or project_lower.startswith(word):
                    return {'name': project, 'confidence': 0.85, 'match_type': 'partial'}

    # Strategy 3: Fuzzy match for typos
    close = get_close_matches(input_lower, [p.lower() for p in PROJECT_NAMES], n=1, cutoff=0.6)
    if close:
        idx = [p.lower() for p in PROJECT_NAMES].index(close[0])
        return {'name': PROJECT_NAMES[idx], 'confidence': 0.7, 'match_type': 'fuzzy'}

    return None


def _has_strong_session_signals(input_lower: str) -> bool:
    """
    Check for strong quick session signals.

    Returns True if 2+ signals detected across categories.
    """
    signal_count = 0
    for patterns in SESSION_SIGNALS.values():
        for pattern in patterns:
            if re.search(pattern, input_lower):
                signal_count += 1
                if signal_count >= 2:
                    return True
    return False


def _generate_clarification(user_input: str, project_match: dict | None) -> dict:
    """Generate clarification for ambiguous input."""
    if project_match and project_match.get('confidence', 0) >= 0.5:
        return {
            'message': (
                f"I'm not sure what you'd like to do. Did you mean to:\n\n"
                f"1. **Continue your book project** \"{project_match['name']}\"?\n"
                f"2. **Start a quick session** with \"{user_input}\" as the concept?\n\n"
                f"Just say \"1\" or \"2\", or tell me more!"
            ),
            'options': [
                {'key': '1', 'mode': 'book', 'project': project_match['name']},
                {'key': '2', 'mode': 'session', 'concept': user_input}
            ]
        }

    return {
        'message': (
            "I can help with that! Are you looking to:\n\n"
            "1. **Start a quick creative session** (casual, mood-based writing)?\n"
            "2. **Work on a book project** (serious writing with tracking)?\n\n"
            "Or just tell me more about what you have in mind!"
        ),
        'options': [
            {'key': '1', 'mode': 'session'},
            {'key': '2', 'mode': 'book'}
        ]
    }


def _generate_empty_clarification() -> dict:
    """Generate clarification for empty input."""
    project_preview = ', '.join(PROJECT_NAMES[:3]) if PROJECT_NAMES else 'none yet'
    return {
        'message': (
            "What would you like to write today?\n\n"
            "**Quick session ideas:**\n"
            "- \"vampire romance tonight\"\n"
            "- \"something dark and obsessive\"\n"
            "- \"trapped in elevator with my boss\"\n\n"
            "**Or continue a book project:**\n"
            f"- Available: {project_preview}"
        ),
        'options': []
    }


def _generate_project_list_clarification(context: str) -> dict:
    """Generate clarification showing available projects."""
    if not PROJECT_NAMES:
        return {
            'message': (
                f"You mentioned {context}, but I don't see any book projects yet.\n\n"
                "Would you like to start a quick creative session instead?"
            ),
            'options': [{'key': 'session', 'mode': 'session'}]
        }

    project_list = '\n'.join(f"- {p}" for p in PROJECT_NAMES)
    return {
        'message': (
            f"Which project did you mean for {context}?\n\n"
            f"Available projects:\n{project_list}\n\n"
            "Just name the one you want to continue!"
        ),
        'options': [{'key': p, 'mode': 'book', 'project': p} for p in PROJECT_NAMES]
    }


if __name__ == '__main__':
    # Test the router
    test_inputs = [
        "continue my-novel chapter 4",
        "vampire romance tonight",
        "something dark and obsessive",
        "continue",
        "start a new book",
        "write a novel",
        "cunning thief",
        "dark romance",
        "",
    ]

    print("Input Router Tests")
    print("=" * 60)

    for test in test_inputs:
        result = route_input(test)
        print(f"\nInput: \"{test}\"")
        print(f"  Mode: {result.mode} (confidence: {result.confidence:.2f}, tier: {result.match_tier})")
        if result.project_name:
            print(f"  Project: {result.project_name}")
        if result.chapter:
            print(f"  Chapter: {result.chapter}")
        if result.entry_type:
            print(f"  Entry type: {result.entry_type}")
        if result.initial_concept:
            print(f"  Concept: {result.initial_concept}")
        print(f"  Reasoning: {result.reasoning}")
        if result.clarification:
            print(f"  Clarification: {result.clarification['message'][:60]}...")
