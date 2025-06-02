import pytest
from selenium import webdriver
from selenium.webriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--user_lang", action="store", default=None, help="Choose your language")


@pytest.fixture
def browser(request):
    print("\nSTART...\n")
    user_lang = request.config.getoption("user_lang")
    browser = webdriver.Chrome()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    yield browser
    print("\nFINISH...\n")
    browser.quit()
