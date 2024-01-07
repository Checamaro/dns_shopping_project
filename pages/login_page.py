from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_Page(Base):
    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    enter_button = "//div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]"
    enter_via_pass_button = "//div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]"
    email = "//div[1]/div[1]/div[2]/div[1]/input[1]"
    password = "//div[1]/div[1]/div[3]/div[1]/input[1]"
    login_button = "//div[1]/div[1]/div[6]/div[1]/button[1]/span[1]"
    user_menu = "//div[3]/div[2]/div[1]/div[1]/div[2]"
    user_nickname = "//div[1]/div[1]/div[2]/div[1]/div[2]/a[1]"

    # Getters

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_enter_via_pass_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_via_pass_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_user_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_menu)))

    def get_user_nickname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_nickname)))

    # Actions

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Нажатие кнопки 'Войти'")

    def click_enter_via_pass_button(self):
        self.get_enter_button().click()
        print("Нажатие кнопки 'Войти с паролем'")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Ввод почты")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажатие кнопки 'Войти(с введенными данными)'")

    def mouse_point_on_user_menu(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_user_menu().perform())
        print("Наводим мышь на аватар профиля")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.click_enter_via_pass_button()
        self.input_email("kirill.sharevich@yandex.ru")
        self.input_password("qwerty123456")
        self.click_login_button()
        self.mouse_point_on_user_menu()
        self.assert_word(self.get_user_nickname, 'Пришелец-BC48623')
