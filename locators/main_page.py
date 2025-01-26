from selenium.webdriver.common.by import By


class MainPage:

    PERSONAL_ACCOUNT_BUTTON = [By.XPATH,'.//p[text()="Личный Кабинет"]']
    CONSTRUCTOR_BUTTON = [By.XPATH, './/p[text()="Конструктор"]']
    CONSTRUCT_A_BURGER_LINE = [By.XPATH, './/h1[text()="Соберите бургер"]']
    ORDERS_LINE_BUTTON = [By.XPATH, '//p[text()="Лента Заказов"]']
    ORDERS_LINE_HEADER = [By.XPATH, '//h1[text()="Лента заказов"]']
    R2_D3_BUN = [By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]']
    INGREDIENT_DETAILS_HEADER = [By.XPATH, '//h2[text()="Детали ингредиента"]']
    CLOSE_WINDOW_BUTTON = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]']
    BURGER_CONSTRUCTOR_BASKET = [By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]']
    COUNTER = [By.XPATH, '//p[contains(@class, "counter_counter") and text()=2]']
    LOG_IN_BUTTON = [By.XPATH, '//button[text()="Войти в аккаунт"]']
    MAKE_ORDER_BUTTON = [By.XPATH, '//button[text()="Оформить заказ"]']
    ORDERS_NUMBER_IN_CONFIRMATION_WINDOW = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2']
    ORDER_IDENTIFIER = [By.XPATH, '//p[text()="идентификатор заказа"]']
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]/div")
    FIREFOX_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")

