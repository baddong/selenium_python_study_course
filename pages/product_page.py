from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_to_cart(self):
        cart_btn=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        cart_btn.click()

    def test_product_name_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRODUCT_NAME), "Product added is not presented"
        p_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        cart_p_name = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
        print(p_name + ' название товара')
        assert p_name == cart_p_name ,"Wrong product name in cart "

    def test_product_price_in_cart(self):
        p_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_p_price = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE)
        time.sleep(2)
        print(p_price.text + ' цена товара')
        print(cart_p_price.text + ' цена в корзине')
        assert p_price.text == cart_p_price.text, "Wrong  price on product in cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message not disappeared, but should be"
