import allure
from pages.main_page_methods import MainPageMethods
from pages.orders_line_methods import OrdersLineMethods
from pages.personal_account_methods import PersonalAccountMethods


class TestOrdersLine:

    @allure.title('Проверка появления окна Детали заказа')
    def test_order_details_window_appear(self, driver):
        driver_instance, driver_name = driver
        main_page = MainPageMethods(driver_instance)
        orders_line = OrdersLineMethods(driver_instance)
        main_page.click_orders_line_button(driver_name)
        orders_line.click_orders_card()

        assert orders_line.find_content_in_details_header()

    @allure.title('Проверка появления номера заказа из истории заказов в ленте заказов')
    def test_orders_number_from_history_in_orders_line(self, driver, use_token, create_user_order_and_delete):
        driver_instance, driver_name = driver
        main_page = MainPageMethods(driver_instance)
        orders_line = OrdersLineMethods(driver_instance)
        personal_account = PersonalAccountMethods(driver_instance)
        main_page.click_personal_account_button()
        personal_account.click_orders_history_button()
        order_number = personal_account.get_orders_number()
        main_page.click_orders_line_button(driver_name)

        assert orders_line.find_orders_number_in_the_line(order_number)

    @allure.title('Проверка увеличения числа заказов в разделе Выполнено за всё время после нового заказа')
    def test_increase_number_in_done_for_all_time(self, driver, use_token):
        driver_instance, driver_name = driver
        main_page = MainPageMethods(driver_instance)
        orders_line = OrdersLineMethods(driver_instance)
        main_page.click_orders_line_button(driver_name)
        quantity_before_new_order = orders_line.get_orders_quantity_for_all_time()
        main_page.click_constructor_button()
        main_page.click_log_in_button(driver_name)
        main_page.add_ingredient_to_basket()
        main_page.click_make_order_button()
        main_page.click_close_confirmation_window_button(driver_name)
        main_page.click_orders_line_button(driver_name)
        quantity_after_new_order = orders_line.get_orders_quantity_for_all_time()

        assert quantity_before_new_order < quantity_after_new_order

    @allure.title('Проверка увеличения числа заказов в разделе Выполнено за сегодня после нового заказа')
    def test_increase_number_in_done_for_today(self, driver, use_token):
        driver_instance, driver_name = driver
        main_page = MainPageMethods(driver_instance)
        orders_line = OrdersLineMethods(driver_instance)
        main_page.click_orders_line_button(driver_name)
        quantity_before_new_order = orders_line.get_orders_quantity_for_today()
        main_page.click_constructor_button()
        main_page.click_log_in_button(driver_name)
        main_page.add_ingredient_to_basket()
        main_page.click_make_order_button()
        main_page.click_close_confirmation_window_button(driver_name)
        main_page.click_orders_line_button(driver_name)
        quantity_after_new_order = orders_line.get_orders_quantity_for_today()

        assert quantity_before_new_order < quantity_after_new_order

    @allure.title('Проверка появления номера нового заказа в разделе В работе')
    def test_new_orders_number_appears_in_section_in_work(self, driver, use_token):
        driver_instance, driver_name = driver
        main_page = MainPageMethods(driver_instance)
        orders_line = OrdersLineMethods(driver_instance)
        main_page.click_log_in_button(driver_name)
        main_page.add_ingredient_to_basket()
        main_page.click_make_order_button()
        new_order = main_page.get_orders_number_from_confirmation_window()
        main_page.click_close_confirmation_window_button(driver_name)
        main_page.click_orders_line_button(driver_name)

        assert orders_line.find_orders_in_work_list() == '0'+new_order
