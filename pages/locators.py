from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # сслыка на страницу логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # некорректный локатор сслыки на страницу логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    CART_LINK = (By.CSS_SELECTOR, "span > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASS1 = (By.NAME, "registration-password1")
    REGISTER_PASS2 = (By.NAME, "registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.ID, "add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success")]/div[contains(@class,"alertinner")]')


class CartPageLocators(object):
    CART_FORM = (By.XPATH, '//*[@id="content_inner"]/p')  # форма содержимого корзины
    CART_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")  # список товаров в корзине
