""" Модуль содержит функции по работе с JsonPath """

from jsonpath_ng import parse
from logger import logger


def find_by_jsonpath(response, json_path: str):
    """ Поиск в теле ответа по jsonpath

    Args:
        response: тело ответа
        json_path: ключ искомого значения в формате JSONPath

    Returns:
        - str: если получен один элемент по выражению
        - list: если получено более 1-го элемента
    """
    jsonpath_key = parse(json_path)
    jsonpath_value = jsonpath_key.find(response)
    value = list(map(lambda match: match.value, jsonpath_value))

    if len(value) == 0:
        value = str(value)
    if len(value) == 1:
        value = str(value[0])

    logger.info(f'По ключу "{json_path}" получено: {value}')

    return value
