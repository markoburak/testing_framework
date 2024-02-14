import pytest

from utilities import read_configuration
from selenium import webdriver

import time

from components.user_details_page import UserDetailsPage
from components.login_page import LoginPage
from components.main_page import MainPage


class TestUserDetails:
    driver = None

    @pytest.fixture()
    def setup_and_teardown_with_login_user_details(self, request):
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
        time.sleep(0.5)

        loginPage = LoginPage(driver)
        loginPage.login("burakmarko@gmail.com", "12345678")

        main_page = MainPage(driver)
        main_page.nav_open_user_details()

        request.cls.driver = driver

        yield
        driver.quit()

    def test_user_details_first_and_last_names_input(self, setup_and_teardown_with_login_user_details):
        user_details_page = UserDetailsPage(self.driver)
        first_name = user_details_page.get_first_name_input_value()
        last_name = user_details_page.get_last_name_input_value()

        assert first_name == 'Marko'
        assert last_name == 'Burak'
