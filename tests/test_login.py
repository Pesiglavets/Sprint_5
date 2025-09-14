import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pytest
from base_page import BasePage
from locators import MainPageLocators, AuthPageLocators

class TestLogin:
    @pytest.mark.positive
    def test_login_valid_credentials_shows_user_avatar(self, driver, base_url, registered_user):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, registered_user["email"])
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, registered_user["password"])
        page.click(AuthPageLocators.LOGIN_BUTTON)

        assert page.is_element_visible(MainPageLocators.USER_AVATAR)
        assert page.is_element_visible(MainPageLocators.USER_NAME)