
import pytest

from components.main_page import MainPage


@pytest.mark.usefixtures("setup_and_teardown_with_login")
class TestMain:
    driver = None

    def test_main_table_displayed(self):
        main_page = MainPage(self.driver)
        assert main_page.main_table_displayed()
