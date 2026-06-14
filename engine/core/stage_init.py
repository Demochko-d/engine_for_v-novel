import time

from engine.core.stage import Stage

def init_stages(raw_scenes):
    stages = {}
    start_time = time.time()

    for name, scene_data in raw_scenes.items():
        stages[name] = Stage(scene_data)

    print(f'иниализация сцен: успех ({time.time() - start_time} сек.)')
    return stages
