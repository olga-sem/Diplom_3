from locators.personal_account import PersonalAccount
from locators.reset_password import ResetPassword
from pages.base_page_methods import BasePageMethods
import allure


class PersonalAccountMethods(BasePageMethods):
    @allure.step('Поиск кнопки История заказов')
    def find_orders_history_button(self):
        return self.find_element_with_wait(PersonalAccount.ORDERS_HISTORY)

    @allure.step('Клик на кнопку История заказов')
    def click_orders_history_button(self):
        self.click_the_element(PersonalAccount.ORDERS_HISTORY)

    @allure.step('Поиск карточки заказа')
    def find_orders_card(self):
        return self.find_element_with_wait(PersonalAccount.ORDER_CARD)

    def get_orders_number(self):
        return self.get_text_from_element(PersonalAccount.ORDER_NUMBER_IN_ORDER_CARD)

    @allure.step('Клик на кнопку Выход')
    def click_exit_button(self):
        self.click_the_element(PersonalAccount.EXIT_BUTTON)

    @allure.step('Поиск кнопки Вход')
    def find_log_in_button(self):
        return self.find_element_with_wait(ResetPassword.LOG_IN_BUTTON)
