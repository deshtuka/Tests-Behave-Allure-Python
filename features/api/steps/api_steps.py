"""
Модуль содержит шаги для работы с сайтом
"""

from behave import step
from features.api.request.api_request import FreeFootballAPI


@step('Получить информацию о стадионах страны "{area_id}"')
def get_info_about_country_stadiums(context, area_id):
    context.response = FreeFootballAPI().get_areas_by_id(area_id=area_id)


@step('Получить информацию о внутренних турнирах страны "{areas}"')
def get_info_about_national_domestic_tournaments(context, areas):
    query_params = {'areas': areas}
    context.response = FreeFootballAPI().get_competitions(query_params=query_params)


@step('Получить данные игрока с id "{person_id}"')
def get_info_person(context, person_id):
    context.response = FreeFootballAPI().get_person_by_id(person_id=person_id)
