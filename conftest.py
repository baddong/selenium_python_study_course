from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name',action='store',default ="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--languages',action='store',default='en', help="Choose languages for browser")

# Реализовано, только для браузера Chrome
@pytest.fixture(scope ="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    languages = request.config.getoption("languages")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': languages})
    if browser_name == "chrome":
        browser=webdriver.Chrome(options=options)
        browser.implicitly_wait(30)
        print("Start browser Chrome")
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
        print("start browser firefox")
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield  browser
    print("close browser")
    browser.quit()
