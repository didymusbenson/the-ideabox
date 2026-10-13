#!/usr/bin/env python3
"""
UserPromptSubmit Hook: Remind Claude about MC autonomy and sub-agents.

Fires when user submits a prompt. Output is added to Claude's context.

Configuration is read from config.py - edit that file, not this one.
Uses state_manager.py for all path operations (pathlib-based).
"""
import json
import sys
from pathlib import Path

# Add hooks directory to path for local imports
hooks_dir = Path(__file__).resolve().parent
if str(hooks_dir) not in sys.path:
    sys.path.insert(0, str(hooks_dir))

# Import from state_manager for path operations
try:
    from state_manager import get_project_root, read_state
except ImportError as e:
    print(f"Hook error: Cannot import state_manager: {e}", file=sys.stderr)
    # Define minimal fallbacks
    def get_project_root():
        return Path(__file__).resolve().parent.parent.parent
    def read_state(filename):
        return {}

# Import configuration from config.py in the same directory
try:
    from config import MC_NAME, CHARACTER_POV, COACHING_AGENTS
except ImportError:
    # Fallback if config.py doesn't exist or has issues
    MC_NAME = "MC"
    CHARACTER_POV = "the characters"
    COACHING_AGENTS = []


def main():
    """
    Main hook function - outputs roleplay reminders to stdout.

    Reads JSON from stdin (Claude Code input), outputs reminder text.
    Always exits 0 (never blocks).
    """
    try:
        # Read input from stdin (Claude Code provides JSON)
        try:
            input_data = json.load(sys.stdin)
        except (json.JSONDecodeError, EOFError):
            input_data = {}

        # Check if config has been customized
        config_warning = ""
        if "{{" in MC_NAME or "{{" in CHARACTER_POV:
            config_warning = """
!!! CONFIG NOT SET UP !!!
Edit .claude/hooks/config.py to set MC_NAME and CHARACTER_POV
!!! CONFIG NOT SET UP !!!
"""

        # Print reminders - these get added to Claude's context
        print()
        print("=" * 60)
        print("ROLEPLAY REMINDER - READ BEFORE RESPONDING")
        print("=" * 60)
        if config_warning:
            print(config_warning)
        print()
        print("MC AUTONOMY RULES:")
        print(f"- User controls MC ({MC_NAME}). You control all other characters.")
        print("- Do NOT write dialogue for MC that user didn't provide")
        print("- Do NOT embellish MC's actions beyond what user said")
        print("- Do NOT describe MC's internal state or feelings")
        print("- Do NOT add details user didn't specify")
        print("- GOLDEN RULE: If user didn't write it, MC didn't do it.")
        print()
        print("OOC RECOGNITION:")
        print("- ((OOC: text)) or ((text)) = user speaking OUT OF CHARACTER")
        print("- Respond out-of-character - no prose, answer directly")
        print("- Mixed messages: handle OOC direction first, then write scene")
        print("- NEVER ignore double parentheses - always treat as OOC")
        print()
        print("PC PROTECTION (CHARACTER SHEETS ARE GROUND TRUTH):")
        print("- READ character sheets in characters/ BEFORE writing")
        print("- Character sheets OVERRIDE conversation memory after compaction")
        print("- NEVER invent PC details - empty fields are sacred gaps")
        print("- Write AROUND missing PC info, never fill it in")
        print("- Max 1 [OOC] sidebar per scene for missing PC details")
        print("- NPC sheets are auto-logged - update after developing NPC traits")
        print()
        print("=" * 60)
        print("AGENTS (6 consolidated)")
        print("=" * 60)
        print()
        print("CORE:")
        print("  - writer              : Write scene response (ALWAYS runs)")
        print("  - state               : Check tracking files, scene state")
        print()
        print("ANALYSIS:")
        print("  - analyzer quick      : Emotions + intent (default)")
        print("  - analyzer deep       : Full analysis with foresight")
        print("  - analyzer character  : Emotions + intent + observations")
        print("  - analyzer story      : Tension + pacing focus")
        print()
        print("GENERATION:")
        print("  - creator brainstorm  : Ideas when stuck")
        print("  - creator character   : Create new NPC")
        print("  - creator world       : Expand world/lore")
        print("  - creator voice       : Multi-character voice contrast")
        print("  - creator twist       : Inject complications")
        print()
        print("TACTICS:")
        print("  - strategist romance  : Seduction tactics")
        print("  - strategist offense  : Scheme planning")
        print("  - strategist defense  : Detect NPC plots")
        print("  - strategist factions : Political dynamics")
        print()
        print("ROUTING:")
        print("  - router              : Recommend agents for scene")
        print()

        # Print coaching agents if any are defined
        if COACHING_AGENTS:
            print("COACHING (project-specific):")
            for agent_name, description in COACHING_AGENTS:
                print(f"  - {agent_name:<17} : {description}")
            print()

        print("=" * 60)
        print("ORCHESTRATOR PROTOCOL - FOLLOW THIS EVERY RESPONSE")
        print("=" * 60)
        print()
        print("You are a COORDINATOR. Sub-agents write the prose. You direct.")
        print()
        print("1. EXPLORE FIRST: Read characters/, tracking files, scene state")
        print("2. ASSESS: Simple -> writer only. Complex -> analyzer + writer.")
        print("         Seduction -> strategist romance. Unsure -> router.")
        print("3. LAUNCH AGENTS: Do NOT write prose yourself. Use writer agent.")
        print("4. EVALUATE: Check agent output against character sheets.")
        print("   If wrong -> kick back with feedback.")
        print("5. OUTPUT: Print the final prose as clean text in your response.")
        print("   The user reads in a terminal. Diffs and edits are unreadable")
        print("   as prose. Always output the clean, final narrative text.")
        print("6. AFTER WRITING: Update tracking files. Log NPC developments.")
        print("   Do this EVERY TIME. Do not ask permission. Just do it.")
        print()
        print(f"Write ONLY from {CHARACTER_POV}'s POV.")
        print("Do NOT write prose yourself - launch the writer agent.")
        print("Do NOT ask permission for mandatory tasks - just do them.")
        print("=" * 60)

    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)

    sys.exit(0)


if __name__ == '__main__':
    main()
