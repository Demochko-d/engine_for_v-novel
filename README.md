# Engine for V-Novel

A small Python/Pygame engine prototype for a visual novel.

## Requirements

- Python 3.10+
- pygame

## Run

Install dependencies, then start the game:

```powershell
pip install pygame
python game.py
```

## Project Layout

- `game.py` - application entry point.
- `game_config.py` - basic game settings.
- `list_stage.py` - scene definitions and branching choices.
- `core/` - engine code for stages, UI, saving/loading, and asset loading.
- `assets/error.png` - fallback image used when a scene asset is missing.

## Notes

Generated save files are intentionally ignored by git. Add your own background,
character, and music assets locally when building a novel.
