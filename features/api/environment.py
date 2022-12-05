"""
Модуль содержит базовые функции фреймворка для запуска автотестов
"""

from API.api_library import APILibrary
from config import FILE_DEBUG
from utils.logger_func import logger

import os


def before_scenario(context, scenario):
    """ Выполняется вначале каждого сценария

    Args:
        context: контекст сценария.
        scenario: экземпляр Scenario.
    """
    # Экземпляр класса запросов
    context.api_lib = APILibrary()


def after_scenario(context, scenario):
    """ Выполняется после каждого сценария

    Args:
        context: контекст сценария.
        scenario: экземпляр Scenario.
    """
    message = '[SCENARIO] Конец выполнения: ' + scenario.name
    logger.info(message)

    # if scenario.status.name == 'failed' and context.browser:
    #     use_fixture(fixtures.save_test_data_for_allure, context)


def before_all(context):
    """ Выполняется перед запуском тестов

    Args:
        context: контекст сценария.
    """
    # Тестовые данные (на уровне всего тестового прогона)
    context.config.test_data = dict()

    # Очистка "старых" логов прогонов
    os.remove(FILE_DEBUG)

    # импорт всех модулей в папке pulse_api (для корректной работы метода __subclasses__() класса PulseAPILibrary)
    from API import api_requests, api_library, common_steps

    # utils.import_all_modules_from_dir_and_sub_dirs(dir_path=config.PULSE_API_LIB_DIR)
