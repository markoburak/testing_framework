from selenium import webdriver
import pytest

import time

from components.login_page import LoginPage
from utilities import read_configuration


@pytest.fixture()
def setup_and_teardown(request):
    config = read_configuration()

    url = config["general"]["url"]
    browser = config["general"]["browser"]

    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Browser not provided")

    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    time.sleep(0.5)
    yield
    driver.quit()


@pytest.fixture()
def setup_and_teardown_with_login(request):
    config = read_configuration()

    url = config["general"]["url"]
    browser = config["general"]["browser"]

    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Browser not provided")

    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    time.sleep(0.5)

    loginPage = LoginPage(driver)
    loginPage.login("burakmarko@gmail.com", "12345678")
    yield
    driver.quit()

