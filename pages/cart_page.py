from .base_page import BasePage
from .locators import CartPageLocators
import time

class CartPage(BasePage):

    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_SUMMARY), \
            "Cart summary is presented, but should not be"

    def zero_products_in_cart(self):
        zero_cart = self.browser.find_element(*CartPageLocators.CART_FORM).text
        print(zero_cart)
        assert 'Ваша корзина пуста' or 'Your basket is empty' or 'Votre panier est vide' in zero_cart, "No text says cart is empty"
