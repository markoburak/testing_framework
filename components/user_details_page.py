# 3rd party imports

# built-in imports

# local imports
from components.comp_shared import CompShared


class UserDetailsSelectors:
    selectors = {}
    selectors['first_name_input'] = "//*[@id = 'first_name']"
    selectors['last_name_input'] = "//*[@id = 'last_name']"


class UserDetailsPage(CompShared, UserDetailsSelectors):
    def __init__(self, driver):
        super().__init__(driver)

    def get_first_name_input_value(self) -> str:
        return self.get_element_value(selector=self.selectors['first_name_input'])

    def get_last_name_input_value(self) -> str:
        return self.get_element_value(selector=self.selectors['last_name_input'])
