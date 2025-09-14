import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pytest
from base_page import BasePage
from locators import MainPageLocators, AuthPageLocators


class TestRegistration:
    @pytest.mark.positive
    def test_registration_valid_credentials_shows_user_avatar(self, driver, base_url, standard_password, generate_email):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.click(AuthPageLocators.NO_ACCOUNT_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, generate_email)
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, standard_password)
        page.send_keys(AuthPageLocators.CONFIRM_PASSWORD_INPUT, standard_password)   
        page.click(AuthPageLocators.CREATE_ACCOUNT_BUTTON)

        assert page.is_element_visible(MainPageLocators.USER_AVATAR)
        assert page.is_element_visible(MainPageLocators.USER_NAME)


    @pytest.mark.parametrize('invalid_email', ['@testmail.com', 'testmail@.com', 'testmail_gmail.com'])
    def test_registration_invalid_email_shows_error(self, driver, base_url, standard_password, invalid_email):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.click(AuthPageLocators.NO_ACCOUNT_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, invalid_email)
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, standard_password)
        page.send_keys(AuthPageLocators.CONFIRM_PASSWORD_INPUT, standard_password)
        page.click(AuthPageLocators.CREATE_ACCOUNT_BUTTON)

        assert page.is_element_visible(AuthPageLocators.ERROR_FIELD)
        assert page.is_element_visible(AuthPageLocators.ERROR_MESSAGE)

    @pytest.mark.negative
    def test_registration_existing_user_shows_error(self, driver, base_url, standard_password, generate_email):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.click(AuthPageLocators.NO_ACCOUNT_BUTTON)
    
        existing_email = generate_email
        
        page.send_keys(AuthPageLocators.EMAIL_INPUT, existing_email)
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, standard_password)
        page.send_keys(AuthPageLocators.CONFIRM_PASSWORD_INPUT, standard_password)
        page.click(AuthPageLocators.CREATE_ACCOUNT_BUTTON)
        page.click(MainPageLocators.LOGOUT_BUTTON)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.click(AuthPageLocators.NO_ACCOUNT_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, existing_email)
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, standard_password)
        page.send_keys(AuthPageLocators.CONFIRM_PASSWORD_INPUT, standard_password)
        page.click(AuthPageLocators.CREATE_ACCOUNT_BUTTON)
        
        assert page.is_element_visible(AuthPageLocators.ERROR_FIELD)
        assert page.is_element_visible(AuthPageLocators.ERROR_MESSAGE)