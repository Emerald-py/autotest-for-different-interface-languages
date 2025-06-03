import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose your language")
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture
def browser(request):
    print("\nSTART...\n")
    user_lang = request.config.getoption("language")
    user_browser = request.config.getoption("browser_name")
    if user_browser == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
    elif user_browser == "firefox":
        profile = FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_lang)
        options = FirefoxOptions()
        options.profile = profile
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nFINISH...\n")
    browser.quit()
