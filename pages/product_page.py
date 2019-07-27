from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import math
import time

class ProductPage(BasePage):

	def add_to_cart(self):
		cart_btn=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
		cart_btn.click()

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			print("Your code: {}".format(alert.text))
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")


	def test_product_name_in_cart(self):
		assert self.is_element_present(*ProductPageLocators.CART_PRODUCT_NAME), "Product added is not presented"
		p_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		cart_p_name = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
		print(p_name + ' название товара')
		assert p_name in cart_p_name ,"Wrong product name in cart "

	def test_product_price_in_cart(self):
		p_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		cart_p_price = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE)
		time.sleep(2)
		print(p_price.text + ' цена товара')
		print(cart_p_price.text + ' цена в корзине')
		assert p_price.text == cart_p_price.text, "Wrong  price on product in cart"
