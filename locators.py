from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_AVATAR = (By.XPATH, ".//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    CARD = (By.CLASS_NAME, 'card')

class AuthPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    ALREADY_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Уже есть аккаунт')]")   
    ERROR_MESSAGE = (By.XPATH, "//span[contains(text(), 'Ошибка')]")
    WRONG_LOGIN_PASSWORD_MESSAGE = (By.XPATH, "//span[contains(text(), 'Логин или пароль неверны')]")
    ERROR_FIELD = (By.CSS_SELECTOR, "div.input_inputError__fLUP9")
    UNAUTHORIZED_AD_MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

class CreateAdPageLocators:
    ITEM_NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    ITEM_DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea[name='description']")
    ITEM_PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price']")
    AD_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "input[name='category'] + button")
    CATEGORY_OPTION_BOOKS = (By.XPATH, "//span[contains(text(), 'Книги')]")
    CITY_DROPDOWN = (By.CSS_SELECTOR, "input[name='city'] + button")
    CITY_OPTION_SPB = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")
    CONDITION_USED_RADIO = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")

class MyAccountLocators:
    CREATED_TEST_AD_TITLE = (By.XPATH, "//h2[contains(text(), 'Тестовое объявление')]")