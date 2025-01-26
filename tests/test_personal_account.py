import allure
from pages.main_page_methods import MainPageMethods
from pages.personal_account_methods import PersonalAccountMethods


class TestPersonalAccount:

    @allure.title('Проверка открытия личного кабинета после клика на кнопку Личный кабинет на главной странице')
    def test_open_personal_account_with_its_button_in_header(self, driver, use_token):
        main_page = MainPageMethods(driver)
        personal_account_page = PersonalAccountMethods(driver)
        main_page.click_personal_account_button()

        assert personal_account_page.find_orders_history_button()

    @allure.title('Проверка открытия истории заказов после клика на кнопку История заказов в личном кабинете')
    def test_open_orders_history(self, driver, use_token, create_user_order_and_delete):
        main_page = MainPageMethods(driver)
        personal_account_page = PersonalAccountMethods(driver)
        main_page.click_personal_account_button()
        personal_account_page.click_orders_history_button()

        assert personal_account_page.find_orders_card()

    @allure.title('Проверка выхода из личного кабинета после клика на кнопку Выход в личном кабинете')
    def test_exit_personal_account(self, driver, use_token):
        main_page = MainPageMethods(driver)
        personal_account_page = PersonalAccountMethods(driver)
        main_page.click_personal_account_button()
        personal_account_page.click_exit_button()

        assert personal_account_page.find_log_in_button()

