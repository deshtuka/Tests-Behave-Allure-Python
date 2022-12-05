"""
Модуль для работы с запросами API
"""

from utils import logger_func as logger

import requests


class APIRequests:
    """Класс для работы с http-запросами"""

    @staticmethod
    def send_request(url: str, method: str, headers=None, timeout=None, data=None, params=None) -> requests.Response:
        """Отправить запрос.

        Args:
            url: url адрес для отправки запроса
            method: тип запроса. (POST, GET, PUT и т.д.)
            headers: заголовки запроса.
            timeout: время ожидания ответа от сервера в секундах.
            data: тело запроса.
            params: параметры запроса.

        Returns:
            response: объект класса requests.Response.
        """
        try:
            response = requests.request(
                method=method, url=url, timeout=timeout, headers=headers, data=data, params=params, verify=False
            )
        except requests.exceptions.ConnectTimeout as error:
            logger.log_display(data={f'Время ожидания запроса "{timeout}" от удаленного сервера истекло': error},
                               level='ERROR')
            raise error
        except requests.exceptions.SSLError as error:
            logger.log_display(data={f'Ошибка сертификата': error}, level='ERROR')
            raise error
        except requests.exceptions.RequestException as error:
            logger.log_display(data={'Произошло неоднозначное исключение при обработке запроса': error}, level='ERROR')
            raise error
        else:
            logger.log_request_response(response=response)

        return response
