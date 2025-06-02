import pytest
from selenium import webdriver
from selenium.webriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose your language")
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture
def browser(request):
    print("\nSTART...\n")
    user_lang = request.config.getoption("language")
    user_browser = request.config.getoption("browser_name")
    if user_browser == "chrome":
        browser = webdriver.Chrome()
    elif user_browser == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    yield browser
    print("\nFINISH...\n")
    browser.quit()
