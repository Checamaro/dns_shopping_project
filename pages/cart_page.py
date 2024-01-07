from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_Page(Base):

    def __init__(self, driver, main_page):
        super().__init__(driver)
        self.driver = driver
        self.main_page = main_page

    # Locators

    checkout_button = "//div[5]/div[1]/div[1]/button[1]/span[1]"
    cart_product_title = "//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_cart_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_title)))

    # Actions

    def test_compare_titles(self):
        title_on_main_page = self.main_page.get_product_title()
        title_on_cart_page = self.get_cart_product_title()

        # Проверка, что названия совпадают частично (На этом сайте товар в корзине имеет сокращенный вид)
        assert title_on_main_page in title_on_cart_page, f"Названия не совпадают. {title_on_main_page} не является частью {title_on_cart_page}"
        assert len(title_on_cart_page) - len(
            title_on_main_page) < 20, "Допустимое расстояние между названиями превышено"

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    def product_buying(self):
        self.get_current_url()
        self.click_checkout_button()
