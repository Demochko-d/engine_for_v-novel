# Engine for V-Novel

A small Python/Pygame engine prototype for a visual novel.

## Requirements

- Python 3.10+
- pygame

## Run

Install dependencies, then start the game:

```powershell
pip install pygame
python main.py
```

## Project Layout

- `main.py` - application entry point.
- `engine/app.py` - game loop setup.
- `engine/config/` - basic game settings.
- `engine/scenes/` - scene definitions and branching choices.
- `engine/core/` - engine code for stages, UI, saving/loading, and asset loading.
- `assets/bg/` - background images.
- `assets/units/` - character sprites.
- `assets/music/` - music and audio files.
- `assets/error.png` - fallback image used when a scene asset is missing.
- `saves/` - local save files created while playing.

## Notes

Generated save files are intentionally ignored by git. Add your own background,
character, and music assets locally when building a novel.

# Engine for V-Novel

Небольшой прототип движка визуальной новеллы на Python/Pygame.

## Требования

- Python 3.10+
- pygame

## Запуск

Установите зависимости, затем запустите игру:

```powershell
pip install pygame
python main.py
```

## Структура проекта

- `main.py` - точка входа в приложение.
- `engine/app.py` - настройка игрового цикла.
- `engine/config/` - базовые настройки игры.
- `engine/scenes/` - описания сцен и вариантов выбора.
- `engine/core/` - код движка: сцены, UI, сохранение/загрузка и загрузка ассетов.
- `assets/bg/` - фоновые изображения.
- `assets/units/` - спрайты персонажей.
- `assets/music/` - музыка и аудиофайлы.
- `assets/error.png` - изображение-заглушка, если ассет сцены не найден.
- `saves/` - локальные файлы сохранений, созданные во время игры.

## Заметки

Сгенерированные файлы сохранений специально игнорируются git. Добавляйте свои
фоны, персонажей и музыку локально при создании новеллы.
