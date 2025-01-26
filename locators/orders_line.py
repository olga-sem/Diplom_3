from selenium.webdriver.common.by import By


class OrdersLine:
    ORDERS_LINE_HEADER = [By.XPATH, '//h1[text()="Лента заказов"]']
    ORDER_CARD = [By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]']
    ORDER_NUMBER_FIELD_FOR_REPLACEMENT = (By.XPATH, './/*[text()="{order_id}"]')
    ORDERS_LIST = [By.XPATH, '//ul[contains(@class, "OrderFeed_list")]']
    ORDER_DETAILS = [By.XPATH, '//div[contains(@class, "Modal_orderBox")]']
    CONTENT_HEADER = [By.XPATH, '//p[contains(@class, "text text_type_main-medium") and text()="Cостав"]']
    COMPLETED_FOR_ALL_TIME = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']
    COMPLETED_FOR_TODAY = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']
    ORDERS_IN_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')
