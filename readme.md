**Запуск сценариев по тегам**:
1) Запуск только @slow -> `behave --tags=slow`
2) Запуск тегов @slow и @wip->`behave --tags=wip,slow`
3) Запуск без тега @slow, только @wip->`behave --tags=wip,-slow`

**Запуск с генерацией отчетов Allure**
`behave -f allure -o allure_result_folder ./features/api/api_test.feature`

