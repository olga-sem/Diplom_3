from locators.orders_line import OrdersLine
from pages.base_page_methods import BasePageMethods
import allure


class OrdersLineMethods(BasePageMethods):
    @allure.step('Клик на карточку заказа')
    def click_orders_card(self):
        self.click_the_element(OrdersLine.ORDER_CARD)

    @allure.step('Поиск слова "состав" в заголовке Детали заказа')
    def find_content_in_details_header(self):
        return self.find_element_with_wait(OrdersLine.CONTENT_HEADER)

    @allure.step('Поиск номера заказа из истории заказов в ленте заказов ')
    def find_orders_number_in_the_line(self, order_number):
        locator = OrdersLine.ORDER_NUMBER_FIELD_FOR_REPLACEMENT
        locator_with_order_number = (locator[0], locator[1].format(order_id=order_number))
        self.find_element_with_wait(locator_with_order_number)
        return self.display_of_element(locator_with_order_number)


    @allure.step('Поиск списка заказов')
    def find_orders_list(self):
        return self.find_element_with_wait(OrdersLine.ORDERS_LIST)

    @allure.step('Получение количества заказов за всё время')
    def get_orders_quantity_for_all_time(self):
        return self.get_text_from_element(OrdersLine.COMPLETED_FOR_ALL_TIME)

    @allure.step('Получение количества заказов за сегодня')
    def get_orders_quantity_for_today(self):
        return self.get_text_from_element(OrdersLine.COMPLETED_FOR_TODAY)

    @allure.step('Поиск номера заказа в разделе В работе')
    def find_orders_in_work_list(self):
        return self.get_text_from_element(OrdersLine.ORDERS_IN_WORK)
