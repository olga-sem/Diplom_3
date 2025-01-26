from selenium.webdriver.common.by import By


class PersonalAccount:
    ORDERS_HISTORY = [By.XPATH, '//a[text()="История заказов"]']
    EXIT_BUTTON = [By.XPATH, './/button[text()="Выход"]']
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    ORDER_NUMBER_IN_ORDER_CARD = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits-default")])[1]')
