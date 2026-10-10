# 👕 AI Outfit Studio

**ThriftDrip's automatic outfit factory.** Generate 10, 100, or more unique
"MY TYPE OUTFIT" fashion posters + Instagram collages — free, from your phone.

## What it does

1. **Generates** headless AI fashion model photos from text prompts (free, no API key)
2. **Removes** backgrounds automatically
3. **Builds** Instagram-ready posters (9:16), carousel cards (4:5), and 4-fit grids (1:1)
   with bold "MY TYPE OUTFIT" titles
4. **Organizes** everything into folders + one downloadable zip

## The tools (all free, all open-source)

| Tool | What it does | Link |
|------|--------------|------|
| [Pollinations.ai](https://github.com/pollinations/pollinations) | Free text-to-image AI, no API key, URL-based | github.com/pollinations/pollinations |
| [rembg](https://github.com/danielgatis/rembg) | AI background removal (25k stars) | github.com/danielgatis/rembg |
| [Pillow](https://python-pillow.org) | Image processing for collages | python-pillow.org |
| [Pollinator](https://github.com/g-aggarwal/Pollinator) | Android app for AI image generation (same free AI) | github.com/g-aggarwal/Pollinator |
| Google Colab | Free cloud computer that runs the notebook | colab.research.google.com |

**Tested 2026-10-10:** Pollinations generation ✅, headless style ✅,
100-prompt uniqueness ✅, all 3 collage templates ✅.
rembg is the industry standard but needs Colab's disk (couldn't install locally).

## 📱 Launch on Android (5 minutes, no coding)

1. Install **Google Colab** app (or open colab.research.google.com in Chrome)
2. Tap **File → Open notebook → GitHub**, enter `dheerajnain7/Thriftdrip`,
   open `ai-outfit-studio/OutfitStudio.ipynb`
   - *Or*: open this direct link: `https://colab.research.google.com/github/dheerajnain7/Thriftdrip/blob/main/ai-outfit-studio/OutfitStudio.ipynb`
3. Tap **Runtime → Run all**
4. Wait. That's it. Download the zip when it finishes.

## 🎯 Your first outfit image (2 minutes)

1. In the notebook, set `N_OUTFITS = 2` in CELL 3
2. Run all cells
3. Check the `posters/` preview at the end — your first 2 AI outfits

## 🔁 Scale up

| Goal | CELL 3 settings | Time |
|------|-----------------|------|
| Test | `N_OUTFITS = 2` | ~2 min |
| Small batch | `N_OUTFITS = 10` | ~7 min |
| Full drop | `N_OUTFITS = 100` | ~1 hour |

To continue: set `START_INDEX` past your last batch (e.g. `10`) and re-run from CELL 4.

## ⚠️ Honest limits

- **Pollinations is free but shared** — occasional "backend busy" (503); the notebook
  auto-retries 3 times. If it keeps failing, wait 10 minutes.
- **Watermark** — a small `pollinations.ai` mark can appear in the corner.
  Crop it out or let the title cover it.
- **Colab timeouts** — free sessions last a few hours; 100 outfits fits, but keep
  the tab open during long runs.
- **AI imagines the clothes** — these are *design concepts*. For real product drops,
  match each poster to an actual Meesho/product listing before promising it to customers.

## Files

- `OutfitStudio.ipynb` — the main system (open in Colab)
- `prompts.py` — 100 unique outfit prompts (tops × bottoms × colors × shoes)
- `collage.py` — poster/card/grid builders (Pillow)
- `README.md` — this file
