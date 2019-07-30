from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #сслыка на страницу логин
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") #некорректный локатор сслыки на страницу логин
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") #форма для авторизации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") #форма для регистрации
    CART_LINK = (By.CSS_SELECTOR, "span > a.btn.btn-default") #ссылк на страницу корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") #иконка юзера
    REGISTER_EMAIL = (By.NAME, "registration-email") #поле ввода email регистрации
    REGISTER_PASS1 = (By.NAME, "registration-password1") #поле ввода пароля регистрации
    REGISTER_PASS2 = (By.NAME, "registration-password2") #поле ввода повтора пароля регистрации
    REGISTER_SUBMIT = (By.NAME, "registration_submit") #кпопка для завершения регистрации


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.ID, "add_to_basket_form") #кнопка корзина
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color") #цена товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") #имя товара
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong") #имя добавленного товара
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong') #цена товара в корзине
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success")]/div[contains(@class,"alertinner")]') #поле о успешном добавлении товара в корзину

class CartPageLocators(object):
    CART_FORM = (By.XPATH, '//*[@id="content_inner"]/p') #форма содержимого корзины
    CART_SUMMARY = (By.CSS_SELECTOR, ".basket_summary") # список товаров в корзине