import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pytest
from base_page import BasePage
from locators import MainPageLocators, AuthPageLocators, CreateAdPageLocators, MyAccountLocators

class TestAdvertisement:
    @pytest.mark.negative
    def test_create_ad_unauthorized_shows_auth_modal(self, driver, base_url):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.CREATE_AD_BUTTON)

        assert page.is_element_visible(AuthPageLocators.UNAUTHORIZED_AD_MODAL_TITLE)

    @pytest.mark.positive
    def test_create_ad_authorized_shows_ad_in_profile(self, driver, base_url, registered_user):
        driver.get(base_url)
        page = BasePage(driver)
        page.click(MainPageLocators.LOGIN_BUTTON)
        page.send_keys(AuthPageLocators.EMAIL_INPUT, registered_user["email"])
        page.send_keys(AuthPageLocators.PASSWORD_INPUT, registered_user["password"])
        page.click(AuthPageLocators.LOGIN_BUTTON)
        page.is_element_visible(MainPageLocators.USER_AVATAR)
        page.click(MainPageLocators.CREATE_AD_BUTTON)
        page.send_keys(CreateAdPageLocators.ITEM_NAME_FIELD, "Тестовое объявление")
        page.send_keys(CreateAdPageLocators.ITEM_DESCRIPTION_FIELD, "Тестовое описание товара")
        page.send_keys(CreateAdPageLocators.ITEM_PRICE_FIELD, "1000")
        page.is_element_visible(MainPageLocators.USER_AVATAR)
        page.click(CreateAdPageLocators.CATEGORY_DROPDOWN)
        page.click(CreateAdPageLocators.CATEGORY_OPTION_BOOKS)
        page.click(CreateAdPageLocators.CITY_DROPDOWN)
        page.click(CreateAdPageLocators.CITY_OPTION_SPB)
        page.click(CreateAdPageLocators.CONDITION_USED_RADIO)       
        page.click(CreateAdPageLocators.AD_SUBMIT_BUTTON)
        page.is_element_visible(MainPageLocators.CARD)
        page.click(MainPageLocators.USER_AVATAR)

        assert page.is_element_visible(MyAccountLocators.CREATED_TEST_AD_TITLE)