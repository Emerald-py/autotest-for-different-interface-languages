import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default=None, help="Choose your language")


@pytest.fixture
def browser(request):
    print("\nSTART...\n")
    user_lang = request.config.getoption("language")
    user_browser = request.config.getoption("browser_name")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    if user_browser == "chrome":
        browser = webdriver.Chrome()
    elif user_browser == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nFINISH...\n")
    browser.quit()
