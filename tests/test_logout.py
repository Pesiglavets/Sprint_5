import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pytest
from base_page import BasePage
from locators import MainPageLocators, AuthPageLocators

class TestLogout:
    @pytest.mark.positive
    def test_logout_after_login_shows_login_button(self, driver, base_url, registered_user):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.is_element_visible(AuthPageLocators.EMAIL_INPUT)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, registered_user["email"])
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, registered_user["password"])
        page.is_element_visible(AuthPageLocators.LOGIN_BUTTON)
        page.click(AuthPageLocators.LOGIN_BUTTON)
        page.is_element_visible(MainPageLocators.LOGOUT_BUTTON)
        page.click(MainPageLocators.LOGOUT_BUTTON)

        assert page.is_element_visible(MainPageLocators.LOGIN_BUTTON)
        assert not page.is_element_visible(MainPageLocators.USER_AVATAR)
        assert not page.is_element_visible(MainPageLocators.USER_NAME)