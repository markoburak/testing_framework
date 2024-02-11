from Test_cases.TestConfig.base import BaseTest
from components.login_page import LoginPage


class TestLogin(BaseTest):
    driver = None

    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("burakmarko@gmail.com", "12345678")

        assert self.driver.current_url == "https://markoburakpy.pythonanywhere.com/"

    def test_login_with_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("burakmarko@gmail.com", "1234567890")

        assert self.driver.current_url != "https://markoburakpy.pythonanywhere.com/"
