from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_Page(Base):
    url = 'https://www.xcom-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    enter_button = "//div[1]/div[7]/div[2]/div[1]/div[1]"
    email = "//div[2]/input[1]"
    password = "//form[1]/div[3]/input[1]"
    login_button = "//div[5]/input[1]"
    account_logo_button = "//div[1]/div[7]/div[2]/div[2]"
    profile_button = "//div[7]/div[2]/div[2]/div[1]/div[2]/a[1]"
    main_word = "//form[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    login_error = "//form/div[4]"

    # Getters

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_account_logo_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_logo_button)))

    def get_profile_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_login_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_error)))

    # Actions

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Нажатие кнопки 'Войти'")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Ввод почты")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажатие кнопки 'Войти(с введенными данными)'")

    def click_account_logo_button(self):
        self.get_account_logo_button().click()
        print("Нажатие на аватар пользователя")

    def click_profile_button(self):
        self.get_profile_button().click()
        print("Просмотр информации о зарегистрированном пользователе")

    def return_to_main_page(self):
        self.driver.back()
        print("Возврат на главную страницу")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_email("788test567@gmail.com")
        self.input_password("o5emsk7u")
        self.click_login_button()
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            alert.accept()
        except:
            pass
        self.click_login_button()
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            alert.accept()
        except:
            pass
        self.click_account_logo_button()
        self.click_profile_button()
        self.assert_word_f(self.get_main_word, 'Полиграф Шариков')
        self.return_to_main_page()
