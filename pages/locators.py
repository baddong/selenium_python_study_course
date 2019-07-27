from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.ID, "add_to_basket_form") #кнопка корзина
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")      #цена товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") #имя товара
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong") #имя добавленного товара
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong') #цена товара в корзине
