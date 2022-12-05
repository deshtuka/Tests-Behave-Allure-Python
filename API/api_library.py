"""
Модуль содержит базовый класс, являющийся входной точкой для работы с библиотекой API.
"""

from API.api_requests import APIRequests
from config import REQUEST_TIMEOUT

from user_agent import generate_user_agent


class APILibrary(APIRequests):
    """Базовый класс, являющийся входной точкой для работы с библиотекой API сервисов HR платформы."""

    def __init__(self):
        """Инициализация атрибутов классов для работы библиотеки API. """
        super().__init__()

        self.url = None
        self.headers = {'User-Agent': generate_user_agent(device_type="desktop", os='win', navigator='chrome')}
        self.data = {}
        self.params = {}

    def send_request_test(self, method, url, custom_headers: dict = None, data=None, params=None,
                          timeout=REQUEST_TIMEOUT):
        """Отправить запрос на сайт.

        Args:
            method: метод запроса (GET, POST, PUT и т.д.)
            url: адрес для отправки запроса.
            custom_headers: словарь заголовков для запроса.
            data: тело запроса.
            params: словарь query параметров запроса.
            timeout: время ожидания ответа от сервера в секундах.

        Returns:
            response: объект класса requests.Response.
        """
        url = url or self.url

        headers = {}
        headers.update(self.headers)

        if custom_headers:
            headers.update(custom_headers)

        if not data:
            data = self.data

        if not params:
            params = self.params

        response = self.send_request(url=url, method=method, headers=headers, data=data, params=params, timeout=timeout)

        return response
