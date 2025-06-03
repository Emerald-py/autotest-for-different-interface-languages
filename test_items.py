import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(5)
