@all
Feature: Тестовый прогон

  Scenario: Проверка получения данных о стадионах страны
    * Получить информацию о стадионах страны "2195"
    * Статус ответа равен "200"
    * Тело ответа содержит
      | Ключ           | Значение                                 |
      | $.id           | 2195                                     |
      | $.name         | Russia                                   |
      | $.code         | RUS                                      |
      | $.flag         | https://crests.football-data.org/808.svg |
      | $.parentAreaId | 2077                                     |
      | $.parentArea   | Europe                                   |
      | $.childAreas   | []                                       |

  @negative
  Scenario: Проверка получения данных о стадионах страны (негативный)
    * Получить информацию о стадионах страны "9999"
    * Статус ответа равен "404"
    * Тело ответа содержит
      | Ключ      | Значение                                         |
      | $.message | The resource you are looking for does not exist. |
      | $.error   | 404                                              |

  Scenario: Проверка получения данных о внутренних турнирах страны
    * Получить информацию о внутренних турнирах страны "2195"
    * Статус ответа равен "200"
    * Тело ответа содержит
      | Ключ                   | Значение          |
      | $.competitions[0].name | Russian Cup       |
      | $.competitions[1].name | FNL               |
      | $.competitions[2].name | RFPL              |
      | $.competitions[3].name | Playoffs 1/2      |
      | $.competitions[4].name | Russian Super Cup |

  @negative
  Scenario: Проверка получения данных о внутренних турнирах страны (негативный)
    * Получить информацию о внутренних турнирах страны "9999"
    * Статус ответа равен "200"
    * Тело ответа содержит
      | Ключ                   | Значение |
      | $.count                | 0        |
      | $.filters.areas[0]     | 9999     |
      | $.filters.competitions | []       |

  @negative
  Scenario: Проверка получения данных об игроке - доступ запрещён (негативный)
    * Получить данные игрока с id "44"
    * Статус ответа равен "403"
    * Тело ответа содержит
      | Ключ      | Значение                                                                                                                   |
      | $.message | The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription. |
