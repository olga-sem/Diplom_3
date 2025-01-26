from selenium.webdriver.common.by import By


class ResetPassword:

    RESET_PASSWORD_LINK = [By.LINK_TEXT, "Восстановить пароль"]
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']
    RESET_PASSWORD_BUTTON = [By.XPATH, '//button[text()="Восстановить"]']
    SAVE_BUTTON = [By.XPATH, '//button[text()="Сохранить"]']
    PASSWORD_FIELD = [By.XPATH, './/input[@name="Пароль"]']
    EYE_ICON = [By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]']
    VISIBLE_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]')
    LOG_IN_BUTTON = [By.XPATH, './/button[text()="Войти"]']
