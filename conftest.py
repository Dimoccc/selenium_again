import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: \nes, \nru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    print("\nstart chrome browser language",language, "for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/coders-at-work_207

    yield browser
    print("\nquit browser..")
    browser.quit()