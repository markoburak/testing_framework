import os

import pytest

from Test_cases.TestConfig.base import BaseTest
from components.login_page import LoginPage
from utilities import read_excel


class TestLogin(BaseTest):
    driver = None

    @pytest.mark.parametrize("email, password", read_excel.get_data_from_excel("../ExcelFiles/username.xlsx", "Test valid"))
    def test_login_with_valid_credentials(self, email, password):
        login_page = LoginPage(self.driver)

        login_page.login(email=email, password=password)

        assert self.driver.current_url == "https://markoburakpy.pythonanywhere.com/"

    @pytest.mark.parametrize("email, password", read_excel.get_data_from_excel("../ExcelFiles/username.xlsx", "Test invalid"))
    def test_login_with_invalid_credentials(self, email, password):
        login_page = LoginPage(self.driver)
        login_page.login(email=email, password=password)

        assert self.driver.current_url != "https://markoburakpy.pythonanywhere.com/"
