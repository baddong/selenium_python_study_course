from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.test_product_name_in_cart()
    page.test_product_price_in_cart()

