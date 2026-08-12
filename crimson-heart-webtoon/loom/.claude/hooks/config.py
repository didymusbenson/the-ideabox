"""
Roleplay Configuration - Edit these values for your project.

This is the ONLY file you need to edit for hook customization.
Set MC_NAME and CHARACTER_POV at minimum. Other fields are used
by the system when creating sessions and character sheets.
"""

# =============================================================================
# REQUIRED - You must set these
# =============================================================================
#
# Configured for the CRIMSON HEART webtoon: this is an authored ensemble comic,
# not single-MC roleplay. MC_NAME stays "MC" (anonymous) on purpose so NO
# character is treated as a protected player-character — that lets us develop
# the whole cast, Bunny included. Prefer book-project mode (`_books/`) for the
# actual chapters. See ../../README.md ("Tooling — loom") for how to run it here.

# Your MC's name (the character YOU play). "MC" = anonymous / no protected PC.
MC_NAME = "MC"

# POV instruction - who Claude writes as. Ensemble authoring => everyone.
CHARACTER_POV = "all characters"

# =============================================================================
# OPTIONAL - Add project-specific coaching agents
# =============================================================================

# Format: [("agent-name", "Brief description"), ...]
COACHING_AGENTS = [
    # ("romance-coach", "Guide romantic tension and pacing"),
    # ("combat-advisor", "Choreograph action scenes"),
]
