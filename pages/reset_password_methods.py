import data
from pages.base_page_methods import BasePageMethods
from locators.reset_password import ResetPassword
import data
import allure

class ResetPasswordMethods(BasePageMethods):
    @allure.step('Клик на ссылку Восстановить пароль')
    def click_reset_password_button(self):
        self.click_the_element(ResetPassword.RESET_PASSWORD_LINK)

    @allure.step('Поиск кнопки Восстановить')
    def find_reset_button(self):
        return self.find_element_with_wait(ResetPassword.RESET_PASSWORD_BUTTON)

    @allure.step('Клик на поле Email')
    def click_email_field(self):
        self.click_the_element(ResetPassword.EMAIL_FIELD)

    @allure.step('Добавление почты в поле Почта')
    def add_email_to_email_field(self):
        self.add_text_to_element(ResetPassword.EMAIL_FIELD, data.reset_password_email)

    @allure.step('Клик на кнопку Восстановить в окне ввода почты')
    def click_reset_button(self):
        self.click_the_element(ResetPassword.RESET_PASSWORD_BUTTON)

    @allure.step('Поиск кнопки Сохранить')
    def find_save_button(self):
         return self.find_element_with_wait(ResetPassword.SAVE_BUTTON)

    @allure.step('Клик на поле Пароль')
    def click_password_field(self):
        self.click_the_element(ResetPassword.PASSWORD_FIELD)

    @allure.step('Добавление пароля в поле Пароль')
    def add_password_to_password_field(self):
        self.add_text_to_element(ResetPassword.PASSWORD_FIELD, data.password)

    @allure.step('Клик на иконку скрытия/показа пароля')
    def click_eye_icon(self):
        self.click_the_element(ResetPassword.EYE_ICON)

    @allure.step('Проверка отображения введённого пароля в поле Пароль')
    def check_password(self):
        return self.display_of_element(ResetPassword.VISIBLE_PASSWORD)
