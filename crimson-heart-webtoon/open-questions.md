# Crimson Heart — Open Questions & Parking Lot

Unresolved decisions and ideas to explore, kept visible so they don't get silently
invented or forgotten. Nothing here is canon yet.

## Decks / suit-systems to explore

The world already leans on real card systems — French suits for the heroes'
[core four](./roster.md), Swiss/German suits and the tarot minor arcana for the
other two hero groups, and now **Tujeon** for the [enemy](./antagonists.md). Other
decks are on the table as future flavor:

- **Tujeon (투전)** — *committed.* Now the backbone of the [antagonists](./antagonists.md):
  eight suits, each led by a General, chosen because that command hierarchy is built
  into the game's rules. (Research found no existing media that personifies tujeon +
  its generals, so the framing is ours.)
- **Mughal Ganjifa** — *freed up.* Was the earlier draft for the enemy before tujeon
  won on structure. The eight-suit palette is still available if we ever want it for a
  different faction (e.g. a foreign/rival power) rather than the main enemy.

## Cast / roster

- **Bunny's surname — revisit (working: Shinzo).** *Shinzō* (心臓) is Japanese for
  "heart," a nice fit for Crimson Heart; we're keeping it **for now**. This is a
  deliberately **multicultural** project, though, so the choice is worth a second pass —
  e.g. a Korean route would land closer to **Maeum** (마음, "heart/mind"). Pinned, not
  locked; **no story beats depend on her nationality yet.** (Note: a Japanese surname
  cuts against the earlier idea of tying her homeland to the Korean *tujeon* enemy — fine,
  just don't rely on that thread.)
- **Amber Diamond's role — under review.** "Single mother" is inherited from the early
  roster and may be **replaced entirely.** Until settled: keep it contained to her sheet;
  don't make it load-bearing for other arcs (esp. the Bunny/Amber motherhood mirror,
  which is parked as provisional). Once locked, re-open the "how are Bunny and Amber
  different" mirror question.
- Real-life (civilian) names behind every magical alias. *(Husband **resolved: Matthew
  "Matty" Shinzo**, WFH software engineer — see his sheet. Teammates' civilian names still
  TBD.)*
- Which tarot minor-arcana suit is **Bunny's daughter**, and the rest of that new generation.
- Who the **Swiss/German-suits** group are and when they enter.
- Whether the three hero suit-systems are rivals, allies, successors, or something else.
- **Per-teammate specifics — define as each enters the story:** civilian name, signature
  attack, team-up combos, and her **own coping mechanism** for the shared war trauma
  (each distinct; none is "supporting Bunny"). Fixed now: team combat has solo /
  team-up / combined-ultimate tiers; together they're stronger; the worst threats can't
  be soloed. See `world.md` → *How the core four fight*.

## Enemy

- The **order** Crim faces Generals 2–8 (only the **North Star** is fixed, as her first foe).
- Which of the eight tujeon Generals are the inner circle / true powers vs. lesser leaders.
- Whether the enemy is the **Demon Gang returned** or a new power, and how tujeon ties to that history.
- How broadly the Star suit's **falling-star possession** works beyond the chapter 1 opener.
- Locking a **canonical** tujeon suit/General list + romanization (sources vary slightly).

## Continuity

- **ONE daughter, not two — PILOT ADJUST NEEDED (note only, do not auto-rewrite).** Cast
  is now a **single ~8-year-old daughter** (only child), the same age Bunny was when Kitty
  recruited her. The **drafted opening is built around two kids** and needs reblocking:
  `chapter-1-concept.md` and `pacing.md` (older kid to school + *younger girl* spots the
  star + Bunny & *Kid 2* to the store + *4yo* watching TV at the end), the "mother of
  two" / "two kids" lines in `premise.md` + `README.md`, and the two-kid phrasing in this
  project's `OUTLINE.md` (flagged there too). Simplest reblock: the one daughter is with
  Bunny throughout (star sighting, store, cat, couch) — **author owns the copy.**

### Reconciled

- **Bunny/Matty occupations vs. the SAHM pilot — RESOLVED.** Settled shape: **Matty** is
  an **office-based** software engineer (commutes out); **Bunny** is a **hospice /
  home-health aide** and self-paced nursing student who, **at story start, is on an
  extended break and parenting full-time.** This **matches the drafted Ch.1** (husband
  leaves for work / "at lunch" / drives home; Bunny home with the kids; Ms. Neighbor
  still needed) — **no rewrite required.** The "stay-at-home mother" tags in
  `premise.md`, `roster.md`, `README.md` remain true for story-start; when convenient,
  enrich them to "caregiver on break," but nothing is broken. *(Supersedes the earlier
  RN-practicing / WFH-Matty draft, which had created the conflict.)*

## Deliberate in-text threads (raise, don't pre-answer)

- **Should Bunny go back to work?** She's on an extended break (hospice/home-health aide)
  and parenting full-time. Her possible return is a **character question to explore in the
  story** — tangled with POTS, trauma, the magical-girl intrusion, and her need to be of
  use beyond the home. Don't resolve it in the bible; let scenes earn it.

## Story / craft

- The love interest — **working name "Jack"** (may change); core beats settled (see his
  sheet). Still open: **the content of his whispered last words** — an author-held,
  fixed line to be revealed slowly; keep it blank in drafting until we decide the reveal.
- Serialization plan, art direction, and target platform for the webtoon.

## Tooling

- **loom persistence — RESOLVED.** [`loom/`](./loom/) was **vendored** (committed
  directly into this repo, no longer a submodule), so all loom-authored content is
  tracked and pushed here. Trade-off accepted: we no longer get a one-command pull of
  upstream WintersRain/loom updates; re-syncing upstream would be a manual merge.
- **loom config — RESOLVED.** `config.py` set for ensemble authoring
  (`MC_NAME="MC"`, `CHARACTER_POV="all characters"`). See the README's *Tooling* section.
- **Book project — SCAFFOLDED.** `loom/_books/crimson-heart/` is seeded (world bible,
  6-episode outline, 10 cast sheets). Remaining: start **drafting** scenes into
  `SCENES/` (adapt the [pacing](./pacing.md) beats), and lock the TBD names as we go.
