# Art Direction

## In one line

Dark-fantasy, **hi-res pixel art**: a candlelit psychic parlor — cool and muted — where the tools of
the trade glow with personality against the gloom.

## Mood

- **Dark fantasy.** Ominous, atmospheric, a little unsettling. The parlor is *theater dressed to
  look mystical* — draperies, candlelight, occult clutter.
- **The skeptic's contrast.** The staging is dramatic; the protagonist is the deadpan, guarded
  observer sitting inside it. The art can fully commit to the mysticism while the writing quietly
  undercuts it. That gap is on-brand.

## Fidelity

- **Hi-res pixel art** (Papers-Please-tier detail), not chunky retro. Client portraits must be
  **expressive** — faces carry the emotional read of every visit.

## Palette

Blues, blacks, and purples lead; saturation is rationed.

- **Dominant field — cool & muted:** slate and midnight blues, dusty violets and plums, charcoals and
  near-blacks.
- **Warm counterpoints — sparing:** candle gold, oxblood/wine, parchment cream. Concentrated on the
  divination artifacts and light sources so the tools of the trade read *warm against a cool room*.
  (How far to push warm-vs-fully-cool is an open tuning question.)
- **Pure saturation is a scalpel.** The fully-saturated hues (red, cyan, amber, …) are reserved for
  **rare, meaningful signals** — a magic glow, a danger tell, a UI alert — never large fills.
- Exact hex values are DESIGN work; this file captures intent, not a swatch.

## Composition — the consultation view

A split-screen two-hander (echoes a JRPG battle framing):

- **Client:** top-left, lit and expressive — the "encounter."
- **Player:** bottom-right, a dark **silhouette / profile** — guarded, in keeping with the character.
- **Dialogue choices:** boxed along the bottom.
- **Reference / menu access:** menus to open reference material (e.g., a tarot explainer book) as
  diegetic objects.

## The reading — a separate scene

Performing a reading is **its own scene**, distinct from the consultation chat. Presentation is one
of (open question):

- a **dim-background modal overlay** (the reading interface layers over the parlor), or
- a **full transition** to a dedicated reading-table view.

Either way it's a distinct scene, and either keeps the reading tactile and focused. The reading table
is the game's **Papers-Please-style workspace**: the deck / hand / chart and the open reference books
laid out, with steps proceeding tactilely — cards turning, palm lines tracing, chart placements
resolving.

## Divination artifacts have personality

The cards, the palm, the star charts, the candles are **characterful, detailed, and warm** — the
visual stars of the game, not generic props. The ornate tarot art in the Zachtronics reference is the
touchstone for *richness and personality*. Whether the artifacts go fully illustrated-ornate or stay
in hi-res pixel is an open call (see open-questions); either way, **personality is the goal**.

## Reference-material UI

Each divination type has an in-world **reference book / menu** — a tarot explainer, a palmistry
guide, an astrology table. These are diegetic objects the player opens during a reading, and they
double as how the player *learns each method's "book."* See
[`divination-methods.md`](./divination-methods.md).

## Touchstones (for feel, not prescription)

- **Papers, Please** — the diegetic workstation and the tactile "deliver the verdict" act.
- **Final Fantasy (NES)** — the framed two-hander / boxed-menu composition.
- **Zachtronics tarot** — richness and personality of the occult artifacts.
- **Mobile pixel RPGs (e.g. BSF)** — legible pixel stat / scorecard panels.

## Open art questions

Tracked in [`open-questions.md`](./open-questions.md): reading-scene presentation (modal overlay vs.
full transition), artifact rendering (ornate-illustrated vs. hi-res pixel), and how far to push the
warm/cool split.
