from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    CART_LINK = (By.CSS_SELECTOR, "span > a.btn.btn-default")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.ID, "add_to_basket_form") #кнопка корзина
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")      #цена товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") #имя товара
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong") #имя добавленного товара
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong') #цена товара в корзине
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success")]/div[contains(@class,"alertinner")]')

class CartPageLocators(object):
    CART_FORM = (By.XPATH, '//*[@id="content_inner"]/p') #форма содержимого корзины
    CART_FORM = (By.XPATH, '//*[@id="content_inner"]/p') #форма содержимого корзины
    CART_SUMMARY = (By.CSS_SELECTOR, ".basket_summary") # список товаров в корзине