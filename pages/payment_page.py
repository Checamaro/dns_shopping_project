from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_registration_word = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"

    # Getters

    def get_product_registration_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_registration_word)))

    # Actions

    # Methods

    def select_product(self):
        self.get_current_url()
        self.assert_word(self.get_product_registration_word(), 'Оформление заказа')
        self.get_screenshot()
