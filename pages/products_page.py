from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Products_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.title_on_product_page = None
        self.title_on_cart_page = None

    # Locators

    sort_by_popularity_button = "//div[1]/span[2]/a[1]"
    filter_by_price_up_to = "//div[2]/input[1]"
    filter_by_manufacturer = "//div[3]/div[2]/div[5]/label[1]/input[1]"
    filter_apply_button = "//div[3]/div[2]/div[5]/a[1]"
    add_to_cart_button = "//div[1]/div[2]/div[4]/div[5]/div[2]/button[1]"
    number_on_cart_icon = "//a[3]/div[1]"
    cart_button = "//div[7]/div[1]/a[3]"

    # Getters

    def get_sort_by_popularity_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_by_popularity_button)))

    def get_filter_by_price_up_to(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_by_price_up_to)))

    def get_filter_by_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_by_manufacturer)))

    def get_filer_apply_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_apply_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_number_on_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_on_cart_icon)))

    # Actions
    def click_sort_by_popularity_button(self):
        self.get_sort_by_popularity_button().click()
        print("Выбираем сортировку по популярности")

    def input_get_filter_by_price_up_to(self, filter_by_price_up_to):
        self.get_filter_by_price_up_to().send_keys(filter_by_price_up_to)
        print("Выбираем лимит по цене ДО")

    def click_filter_by_manufacturer(self):
        self.get_filter_by_manufacturer().click()
        print("Выбираем производителя")

    def click_filer_apply_button(self):
        self.get_filer_apply_button().click()
        print("Показать товары")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Добавить в корзину")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Переходим в корзину")

    # Methods

    def select_product(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_sort_by_popularity_button()
        self.input_get_filter_by_price_up_to("300000")
        self.click_filter_by_manufacturer()
        self.click_filer_apply_button()
        self.click_add_to_cart_button()
        self.assert_word_t(self.get_number_on_cart_icon(), '1')
        self.click_cart_button()
        self.assert_url('https://www.xcom-shop.ru/checkout/')
