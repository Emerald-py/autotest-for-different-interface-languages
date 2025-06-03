from selenium.webdriver.common.by import By
import time


def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button) == 1, "The button is missing"
