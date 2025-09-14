import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture
def base_url():
    return "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture
def standard_password():
    return "StandardPassword123"

@pytest.fixture
def generate_email():
    number = random.randint(10000, 99999)
    random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
    new_email = f'test_mail{random_string}_{number}@gmail.com'
    return new_email

@pytest.fixture
def registered_user(standard_password):
    email = "registered_user@gmail.com"
    return {"email": email, "password": standard_password}