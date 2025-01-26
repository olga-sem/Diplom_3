from pages.base_page_methods import BasePageMethods
from locators.main_page import MainPage
import allure


class MainPageMethods(BasePageMethods):
    @allure.step('Клик на кнопку Личный кабинет')
    def click_personal_account_button(self):
        self.click_the_element(MainPage.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_the_element(MainPage.CONSTRUCTOR_BUTTON)

    @allure.step('Поиск заголовка Соберите бургер')
    def find_constructor_header(self):
        return self.find_element_with_wait(MainPage.CONSTRUCT_A_BURGER_LINE)

    @allure.step('Клик на кнопку Лента Заказов')
    def click_orders_line_button(self, driver_name):
        if driver_name == 'chrome':
            self.wait_for_element_to_disappear(MainPage.FIREFOX_MODAL_WINDOW)
            self.click_the_element(MainPage.ORDERS_LINE_BUTTON)
        else:
            self.click_the_element(MainPage.ORDERS_LINE_BUTTON)

    @allure.step('Поиск заголовка Лента заказов')
    def find_orders_line_header(self):
        return self.find_element_with_wait(MainPage.ORDERS_LINE_HEADER)

    @allure.step('Клик на ингредиент')
    def click_the_ingredient(self):
        self.click_the_element(MainPage.R2_D3_BUN)

    @allure.step('Поиск заголовка Детали ингредиента')
    def find_details_header(self):
        return self.find_element_with_wait(MainPage.INGREDIENT_DETAILS_HEADER)

    @allure.step('Клик по кнопку закрытия окна с деталями')
    def click_close_button(self):
        self.click_the_element(MainPage.CLOSE_WINDOW_BUTTON)

    @allure.step('Добавление ингредиента в корзину')
    def add_ingredient_to_basket(self):
        self.drag_and_drop_element(MainPage.R2_D3_BUN, MainPage.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Получение текста со счётчика')
    def get_text_from_counter(self):
        return self.get_text_from_element(MainPage.COUNTER)

    @allure.step('Клик на кнопку Войти в аккаунт')
    def click_log_in_button(self, driver_name):
        if driver_name == 'chrome':
            self.wait_for_element_to_disappear(MainPage.FIREFOX_MODAL_WINDOW)
            self.click_the_element(MainPage.LOG_IN_BUTTON)
        else:
            self.click_the_element(MainPage.LOG_IN_BUTTON)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_make_order_button(self):
        self.click_the_element(MainPage.MAKE_ORDER_BUTTON)

    @allure.step('Поиск заголовка идентификатор заказа')
    def find_order_identifier(self):
        return self.find_element_with_wait(MainPage.ORDER_IDENTIFIER)

    @allure.step('Получение номера заказа с окна подтверждения заказа')
    def get_orders_number_from_confirmation_window(self):
        self.wait_for_element_to_change_text(MainPage.ORDERS_NUMBER_IN_CONFIRMATION_WINDOW, '9999')
        return self.get_text_from_element(MainPage.ORDERS_NUMBER_IN_CONFIRMATION_WINDOW)

    @allure.step('Клик на кнопку закрытия окна подтверждения заказа')
    def click_close_confirmation_window_button(self, driver_name):
        if driver_name == 'chrome':
            self.wait_for_element_to_disappear(MainPage.FIREFOX_MODAL_WINDOW)
            self.click_the_element(MainPage.CLOSE_WINDOW_BUTTON)
        else:
            self.click_the_element(MainPage.CLOSE_WINDOW_BUTTON)



