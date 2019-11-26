import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: ar, ca, cs, da, de, en-gb,/"
                                                                    "el, es, fi, fr, it, ko, nl, pl, pt, pt, br,/"
                                                                    " ro, ru, sk, uk, zh-hans")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser chrome for test...")
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/'.format(user_language))
    yield browser
    print("\nquit browser..")
    browser.quit()
