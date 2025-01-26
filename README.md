# Diplom_3
Дипломный проект. Задание 3: тестирование UI для приложения Stellar Burgers с помощью паттерна Page Object Model. 
Структура проекта:
1) папка locators содержит локаторы для элементов, требующихся для проведения тестирования. Они разделены следующим образом: 
- главная страница
- лента заказов
- личный кабинет пользователя
- восстановление пароля
2) папка pages содержит методы для написания тестов. Методы разделены по функциональности:
- файл с базовыми методами
- проверка основного функционала приложения
- проверка функционала раздела Лента заказов
- проверка работы личного кабинета
- проверка восстановления пароля
3) папка tests содержит тесты, проверяющие вышеперечисленные аспекты функционал приложения. Тесты также разделены по функционалу.
4) файл conftest содержит:
- метод инициализации драйвера для двух браузеров: Chrome и Firefox 
- фикстуру создания и удаления пользователя.
- фикстуру создания и удаления пользоваля, а также заказа для него.
- фикстуру добавления полученных тестовых данных в драйвер
5) файл data содержит тестовые данные для проверки восстановления пароля.
6) файл requirements содержит список необходимых библиотек для работы с данным проектом.
7) файл urls содержит адрес сервиса и эндпоинты для работы с тестами.
8) файл README содержит описание проекта.
9) файл helpers содержит метод генерации тестовых данных для создания пользователя
10) папка allure_results содержит отчёт о тестировании.