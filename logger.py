""" Модуль по настройке логирования """

from loguru import logger
from config import FILE_DEBUG


logger.add(
    FILE_DEBUG,
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='1 day',
    compression='zip'
)
