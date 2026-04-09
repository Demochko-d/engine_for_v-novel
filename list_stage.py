from core.list_func import *
from game_config import *
SCENES = {
    'start_menu': {
        'text': f'Добро пожаловать в {name_game}',
        'name_unit': "pes",
        'unit': "[ng",
        'bg': 'png',
        'vars_return': (
            {
                'text': 'новая игра',
                'func': new_stage,
                'args': 'начало',
            },
            {
                'text': 'сохранdjnfffvifvinfovneovneonveovgnerongornения',
                'func': new_stage,
                'args': "start_2",
            },
            {
                'text': 'сохранd2140927430rnения',
                'func': None,
                'args': None,
            },

        ),
        'scale_unit': 1,
        'unit_offset_y': 150,
        'unit_offset_x': -150,
    },
    'начало': {
        'text': 'Это была темная ночь, я крепко спал под шум моего старого советского холодильника',
        'name_unit': игорь,
        'unit': игорь,
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'далее...',
                'func': new_stage,
                'args': 'начало2',
            },

        ),
        'scale_unit': 1,
        'unit_offset_y': 150,
        'unit_offset_x': 150,
    },
    'начало2': {
        'text': 'Но счастье мое длилось не долго, примерно в час ночи я проснулся от странного шума....',
        'name_unit': "игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'далее...',
                'func': new_stage,
                'args': 'начало3',
            },

        ),
        'scale_unit': 1,
        'unit_offset_y': 150,
        'unit_offset_x': 150,
    },
    'начало3': {
        'text': 'Кто то стучал ночью по батареям...',
        'name_unit': "игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Подойти к батарее',
                'func': new_stage,
                'args': 'начало5',
            },
            {
                'text': 'Лечь спать обратно',
                'func': new_stage,
                'args': 'начало4',
            }

        ),
        'scale_unit': 0.2,
        'unit_offset_y': -80,
        'unit_offset_x': -600,
    },
    'начало4': {
        'text': 'Понадеявшись что шум продлится недолго я закрыл глаза и попытался заснуть',
        'name_unit': 'игорь',
        'unit': 'игорь',
        'bg': 'черный',
        'vars_return': (
            {
                'text': 'Новая игра',
                'func': new_stage,
                'args': 'начало',
            },

        ),
        'scale_unit': 1,
        'unit_offset_y': -1000,
        'unit_offset_x': 0,
    },
    'начало5': {
        'text': 'Подойдя к батарее шум усилился',
        'name_unit': None,
        'unit': None,
        'bg': 'батарея',
        'vars_return': (
            {
                'text': 'Новая игра',
                'func': new_stage,
                'args': 'начало',
            },

        ),
        'scale_unit': 1,
        'unit_offset_y': -100,
        'unit_offset_x': 0,
    }

}