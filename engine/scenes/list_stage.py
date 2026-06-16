from engine.config.game_config import name_game
from engine.core.list_func import new_stage


SCENES = {
    "start_menu": {
        "text": f"{name_game}\nКороткая демо-сцена: здесь можно посмотреть, какие базовые возможности уже есть в движке.",
        "name_unit": None,
        "unit": None,
        "bg": "demo_start",
        "vars_return": (
            {
                "text": "Начать демо",
                "func": new_stage,
                "args": "engine_overview",
            },
            {
                "text": "О движке",
                "func": new_stage,
                "args": "engine_about",
            },
        ),
        "scale_unit": 1,
        "unit_offset_y": 0,
        "unit_offset_x": 0,
    },
    "engine_overview": {
        "text": "Движок показывает фон, имя говорящего, текст с эффектом печати и кнопки выбора. Сцены описываются обычным словарем Python.",
        "name_unit": "Демо",
        "unit": "demo_character",
        "bg": "demo_room",
        "vars_return": (
            {
                "text": "Показать интерфейс",
                "func": new_stage,
                "args": "ui_features",
            },
            {
                "text": "Показать переходы",
                "func": new_stage,
                "args": "flow_features",
            },
        ),
        "scale_unit": 1,
        "unit_offset_y": 120,
        "unit_offset_x": -120,
    },
    "ui_features": {
        "text": "В интерфейсе уже есть адаптация под размер окна, анимация наведения на кнопки, верхние кнопки сохранения и загрузки, а также меню сохранений.",
        "name_unit": "Интерфейс",
        "unit": "demo_character",
        "bg": "demo_room",
        "vars_return": (
            {
                "text": "К переходам",
                "func": new_stage,
                "args": "flow_features",
            },
            {
                "text": "В меню",
                "func": new_stage,
                "args": "start_menu",
            },
        ),
        "scale_unit": 0.9,
        "unit_offset_y": 120,
        "unit_offset_x": -160,
    },
    "flow_features": {
        "text": "Переходы между сценами идут через затемнение. Выборы могут вести к разным сценам, а состояние текущей сцены можно сохранить в JSON.",
        "name_unit": "Сцены",
        "unit": None,
        "bg": "demo_transition",
        "vars_return": (
            {
                "text": "Вернуться к обзору",
                "func": new_stage,
                "args": "engine_overview",
            },
            {
                "text": "Завершить демо",
                "func": new_stage,
                "args": "demo_finish",
            },
        ),
        "scale_unit": 1,
        "unit_offset_y": 0,
        "unit_offset_x": 0,
    },
    "engine_about": {
        "text": "Это минимальный Python/Pygame-движок для визуальных новелл: сцены, выборы, фон, персонаж, плавные переходы, сохранения и загрузка.",
        "name_unit": None,
        "unit": None,
        "bg": "demo_start",
        "vars_return": (
            {
                "text": "Начать демо",
                "func": new_stage,
                "args": "engine_overview",
            },
            {
                "text": "Назад",
                "func": new_stage,
                "args": "start_menu",
            },
        ),
        "scale_unit": 1,
        "unit_offset_y": 0,
        "unit_offset_x": 0,
    },
    "demo_finish": {
        "text": "Демо закончено. Можно вернуться в начало, нажать сохранение сверху или продолжить расширять список сцен под свою новеллу.",
        "name_unit": "Готово",
        "unit": None,
        "bg": "demo_transition",
        "vars_return": (
            {
                "text": "В главное меню",
                "func": new_stage,
                "args": "start_menu",
            },
        ),
        "scale_unit": 1,
        "unit_offset_y": 0,
        "unit_offset_x": 0,
    },
}
