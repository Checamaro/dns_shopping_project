from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkout_button = "//form[1]/div[1]/div[2]/div[1]/div[1]/div[17]"
    card_item_price = "//div[1]/div[4]/div[1]/div[3]/div[1]"
    total_price = "//form[1]/div[1]/div[2]/div[1]/div[1]/div[14]/div[1]"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_card_item_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_item_price)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    def product_buying(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.assert_prices_match(self.get_card_item_price, self.get_total_price)
        self.click_checkout_button()
        self.get_screenshot()
