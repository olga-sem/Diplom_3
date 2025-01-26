import allure
from pages.main_page_methods import MainPageMethods


class TestMainPage:

    @allure.title('Проверка работы кнопки Конструктор на главной странице')
    def test_constructor_button(self, driver):
        main_page = MainPageMethods(driver)
        main_page.click_constructor_button()

        assert main_page.find_constructor_header()

    @allure.title('Проверка работы кнопки Лента Заказов на главной странице')
    def test_orders_line_button(self, driver):
        main_page = MainPageMethods(driver)
        main_page.click_orders_line_button()

        assert main_page.find_orders_line_header()

    @allure.title('Проверка появления окна с деталями заказа после клика на ингредиент')
    def test_ingredients_details_window_appear(self, driver):
        main_page = MainPageMethods(driver)
        main_page.click_the_ingredient()

        assert main_page.find_details_header()

    @allure.title('Проверка закрытия окна с деталями об ингредиенте кнопкой закрытия (крестик)')
    def test_close_ingredients_details_window_with_close_button(self, driver):
        main_page = MainPageMethods(driver)
        main_page.click_the_ingredient()
        main_page.click_close_button()

        assert main_page.find_constructor_header()

    @allure.title('Проверка изменения числа в счётчике после добавления ингредиента в корзину')
    def test_check_counter_increase_after_adding_ingredient(self, driver):
        main_page = MainPageMethods(driver)
        main_page.add_ingredient_to_basket()

        assert main_page.get_text_from_counter() == '2'

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_authorised_user_can_make_order(self, driver, use_token):
        main_page = MainPageMethods(driver)
        main_page.click_log_in_button()
        main_page.add_ingredient_to_basket()
        main_page.click_make_order_button()

        assert main_page.find_order_identifier()


