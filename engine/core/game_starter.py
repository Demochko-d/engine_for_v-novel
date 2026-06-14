from engine.core import core_config
from engine.core.assets_load import assets_load
from engine.core.game_class import Game
from engine.core.stage_init import init_stages
from engine.scenes.list_stage import SCENES

stages = init_stages(SCENES)

def start_game(stage, screen, main_unit):
    return Game(
        stages=stages,
        screen=screen,
        stage=stages[stage],
        assets_loader=assets_load,
        base_width=core_config.BASE_WIDTH,
        base_height=core_config.BASE_HEIGHT,
        main_unit=main_unit,
    )
