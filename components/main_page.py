# 3rd party imports

# built-in imports

# local imports
from components.comp_shared import CompShared


class MainSelectors:
    selectors = {}
    selectors['main_table'] = "//*[@id='main_table']"
    selectors['nav_user_details_link'] = "//a[contains(@href,'/user_details')]"


class MainPage(CompShared, MainSelectors):
    def __init__(self, driver):
        super().__init__(driver)

    def main_table_displayed(self) -> bool:
        return self.check_display_status_of_element(selector=self.selectors['main_table'])

    def nav_open_user_details(self) -> None:
        return self.click_element(selector=self.selectors['nav_user_details_link'])