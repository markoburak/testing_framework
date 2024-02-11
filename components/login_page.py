# 3rd party imports

# built-in imports

# local imports
from components.comp_shared import CompShared


class LoginSelectors:
    selectors = {}
    selectors['login_email_field'] = "//*[@id='email']"
    selectors['login_password_field'] = "//*[@id='password']"
    selectors['login_button'] = "//button[@form='login']"


class LoginPage(CompShared, LoginSelectors):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email: str, password: str) -> None:
        self.type_message(selector=self.selectors['login_email_field'], message=email)

        self.type_message(selector=self.selectors['login_password_field'], message=password)

        self.click_element(selector=self.selectors['login_button'])
