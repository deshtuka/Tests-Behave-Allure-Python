""" Модуль для работы с запросами api """

from API.api_library import APILibrary


class FreeFootballAPI(APILibrary):
    """Класс для работы с api "football-data.org" version 4
    """

    def __init__(self):
        super().__init__()
        self.url = 'https://api.football-data.org/v4/{path}'

    def get_areas_by_id(self, area_id, path='areas/{area_id}'):
        """ GET-запрос на получение информации о стадионах страны с указанным id """
        url = self.url.format(path=path.format(area_id=area_id))
        response = self.send_request_test(method='GET', url=url)

        return response

    def get_competitions(self, query_params, path='competitions'):
        """ GET-запрос на получение информации о внутренних соревнованиях страны """
        url = self.url.format(path=path)
        self.params = query_params

        response = self.send_request_test(method='GET', url=url)

        return response

    def get_person_by_id(self, person_id, path='persons/{person_id}'):
        """ GET-запрос на получение информации об игроке с указанным id """
        url = self.url.format(path=path.format(person_id=person_id))
        response = self.send_request_test(method='GET', url=url)

        return response
