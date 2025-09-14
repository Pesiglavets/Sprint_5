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

    @pytest.mark.negative
    def test_login_wrong_password_shows_error_message(self, driver, base_url, registered_user):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, registered_user["email"])
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, "WrongPassword123")
        page.click(AuthPageLocators.LOGIN_BUTTON)
        
        assert page.is_element_visible(AuthPageLocators.WRONG_LOGIN_PASSWORD_MESSAGE)
        assert not page.is_element_visible(MainPageLocators.USER_AVATAR)

    @pytest.mark.negative
    def test_login_nonexistent_email_shows_error_message(self, driver, base_url, standard_password):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, "nonexistent@test.com")
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, standard_password)
        page.click(AuthPageLocators.LOGIN_BUTTON)
        
        assert page.is_element_visible(AuthPageLocators.WRONG_LOGIN_PASSWORD_MESSAGE)
        assert not page.is_element_visible(MainPageLocators.USER_AVATAR)