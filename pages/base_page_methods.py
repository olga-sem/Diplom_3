from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

from locators.main_page import MainPage


class BasePageMethods:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_the_element(self, locator):
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавление текста к элементу')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста с элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Проверить видимость элемента')
    def display_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Проверить кликабельность элемента')
    def check_clickability_of_element(self, locator):
        return WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable(locator))

    @allure.step('Передвинуть элемент')
    def drag_and_drop_element(self, element_from, element_to):
        from_element = self.find_element_with_wait(element_from)
        to_element = self.find_element_with_wait(element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    @allure.step('Подождать смены текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 120).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Подождать закрытия элемента')
    def wait_for_element_to_disappear(self, wait_locator=MainPage.MODAL_WINDOW):
        element = self.driver.find_element(*wait_locator)
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(element))
