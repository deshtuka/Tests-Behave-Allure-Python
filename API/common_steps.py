"""
Модуль содержит базовые шаги для работы с api
"""

from behave import step
import json

from utils.json_methods import find_by_jsonpath


@step('Статус ответа равен "{status_code}"')
def step_impl(context, status_code):
    msg = f'Полученный статус кода "{context.response.status_code}" не равен ожидаемому "{status_code}"'
    assert context.response.status_code == int(status_code), msg


@step('Тело ответа содержит')
def response_body_contains(context):
    if not context.table:
        raise 'Не верно задана таблица'

    response = json.loads(context.response.content)

    for row in context.table:
        key, value = row['Ключ'], row['Значение']

        value_path = find_by_jsonpath(response=response, json_path=key)

        msg = f'Ошибка в теле ответа\nОжидаемое значение : {value}\nПолученное значение: {value_path}'
        assert value in value_path, msg
