""" Модуль содержит основные необходимые функции для работы тестов """

import allure
import json


def get_attachment_type(data):
    """ Получаем attachment_type в виде JSON если строка содержит объект типа JSON

    Args:
        data: данные.

    Returns:
        attachment_type: allure тип JSON или TEXT
    """
    try:
        json.loads(data)

    except ValueError:
        return allure.attachment_type.TEXT
    except TypeError:
        return allure.attachment_type.TEXT
    else:
        return allure.attachment_type.JSON


def convert_data_to_allure_attach_format(data, attachment_type):
    """Конвертировать данные для отправки в allure отчет.

    Args:
        data: данные.
        attachment_type: тип данных класса allure.attachment_type

    Returns:
        data: приведенный тип данных.
    """
    if attachment_type == allure.attachment_type.JSON and not isinstance(data, str):
        data = json.dumps(data)

    elif not isinstance(data, str):
        data = str(data)

    return data
