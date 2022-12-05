""" Модуль содержит функции для логирование действий """

from logger import logger
from utils import utils

import allure


def log_request_response(response, level='INFO'):
    """Логирование Запрос/Ответа"""
    log_request(request=response, level=level)
    log_response(response=response, level=level)


def log_request(request, level):
    """Отправленный запрос"""
    msg = {
        'Тип запроса': request.request.method,
        'URL запроса': request.request.url,
        'Headers запроса': request.request.headers,
        'Тело запроса': request.request.body
    }
    log_display(data=msg, level=level)


def log_response(response, level):
    """Полученный ответ"""
    msg = {
        'Код статуса ответа': response.status_code,
        'Headers ответа': response.headers,
        'Тело ответа': response.text
    }
    log_display(data=msg, level=level)


def log_display(data: dict, level: str) -> ...:
    """ Вывод лога запроса/ответа консоль """
    for name, body in data.items():
        logger.log(level, f'{name}: {body}')

        attachment_type = utils.get_attachment_type(data=body)
        body = utils.convert_data_to_allure_attach_format(data=body, attachment_type=attachment_type)
        allure.attach(body=body, name=name, attachment_type=attachment_type)
