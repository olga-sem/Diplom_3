import allure
from pages.main_page_methods import MainPageMethods
from pages.reset_password_methods import ResetPasswordMethods


class TestResetPassword:

    @allure.title('Проверка открытия формы восстановления пароля после клика на кнопку Восстановить пароль')
    def test_open_reset_password_page(self, driver):
        main_page = MainPageMethods(driver)
        reset_password_page = ResetPasswordMethods(driver)
        main_page.click_personal_account_button()
        reset_password_page.click_reset_password_button()

        assert reset_password_page.find_reset_button()

    @allure.title('Проверка работы кнопки Восстановить на странице ввода почты в форме восстановления пароля')
    def test_reset_button_in_email_page(self, driver):
        main_page = MainPageMethods(driver)
        reset_password_page = ResetPasswordMethods(driver)
        main_page.click_personal_account_button()
        reset_password_page.click_reset_password_button()
        reset_password_page.click_email_field()
        reset_password_page.add_email_to_email_field()
        reset_password_page.click_reset_button()

        assert reset_password_page.find_save_button()

    @allure.title('Проверка отображения пароля в поле Пароль после клика на иконка показа/скрытия пароля')
    def test_check_work_of_eye_icon(self, driver):
        main_page = MainPageMethods(driver)
        reset_password_page = ResetPasswordMethods(driver)
        main_page.click_personal_account_button()
        reset_password_page.click_email_field()
        reset_password_page.add_email_to_email_field()
        reset_password_page.click_password_field()
        reset_password_page.add_password_to_password_field()
        reset_password_page.click_eye_icon()

        assert reset_password_page.check_password()
