from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_menu = "//div[5]/div[3]/div[1]/div[2]"
    computers_and_laptops_directory = "//li[1]/a[1]/span[2]"
    laptops_directory = "//div[1]/a[6]"
    directory_name = "//h1[1]"

    # Getters

    def get_catalog_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_menu)))

    def get_computers_and_laptops_directory(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.computers_and_laptops_directory)))

    def get_laptops_directory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptops_directory)))

    def get_directory_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.directory_name)))

    # Actions

    def click_catalog_menu(self):
        self.get_catalog_menu().click()
        print("Кликаем на каталог")

    def click_computers_and_laptops_directory(self):
        self.get_computers_and_laptops_directory().click()
        print("Кликаем 'Компьютеры и ноутбуки'")

    def click_laptops_directory(self):
        self.get_laptops_directory().click()
        print("Кликаем 'Ноутбуки'")

    # Methods

    def getting_product_directory(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_catalog_menu()
        self.click_computers_and_laptops_directory()
        self.click_laptops_directory()
        self.assert_word_t(self.get_directory_title(),
                           'Ноутбуки')
