import datetime
import re
import logging

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word_f(self, word, result):
        value_word = word().text
        assert value_word == result
        print("Подтверждение")

    def assert_word_t(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Подтверждение")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\checa\\PycharmProjects\\pythonProject\\xcom_shop_project\\screen\\' + name_screenshot)
        print('Сделан скриншот оформления заказа')
    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("GOOD value URL")

    """Method assert prices"""

    def assert_prices_match(self, price1_method, price2_method):
        value_price1 = self.extract_numeric_value(price1_method())
        value_price2 = self.extract_numeric_value(price2_method())

        assert value_price1 == value_price2, "Цены не совпадают"
        print("Цены совпадают")

    """Method extract numeric value"""

    def extract_numeric_value(self, element):
        numeric_value = re.search(r'\d+(\.\d{1,2})?', element.text)
        if numeric_value:
            return float(numeric_value.group())
        return None
