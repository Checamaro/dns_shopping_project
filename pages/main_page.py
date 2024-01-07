from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    search_field = "//div[1]/input[1]"
    search_button = "//div[2]/span[2]"
    sorting_list = "//div[2]/a[1]/span[2]"
    sorting_cheap_button = "//div[10]/div[1]/label[1]/span[1]"
    filter_manufacturer = "//div[1]/div[7]/div[1]/div[1]/div[2]/label[1]/span[1]"
    filter_submit_button = "//div[1]/div[2]/div[1]/button[1]"
    add_to_cart_button = "//div[1]/div[4]/button[2]"
    cart = "//div[3]/div[1]/div[1]/a[1]/span[2]"
    main_word = "//div[2]/div[1]/div[1]/div[1]/a[1]/span[1]"
    price = "//div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]"

    # Getters

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_sorting_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_list)))

    def get_sorting_cheap_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_cheap_button)))

    def get_filter_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer)))

    def get_filter_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_submit_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    # Actions

    def click_search_field(self):
        self.get_search_field().click()
        print("Кликаем на поле поиска по сайту")

    def input_desired_item_name(self, search_field):
        self.get_search_field().send_keys(search_field)
        print("Ввод названия товара")

    def click_search_button(self):
        self.get_search_button().click()
        print("Кликаем кнопку поиска")

    def click_sorting_list(self):
        self.get_sorting_list().click()
        print("Кликаем сортировку результатов поиска")

    def click_sorting_cheap_button(self):
        self.get_sorting_cheap_button().click()
        print("Сортируем товары по возрастанию цены")

    def click_filter_manufacturer(self):
        self.get_filter_manufacturer().click()
        print("Выбираем фильтр по производителю")

    def scrolling_to_submit_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_filter_submit_button)
        print("Скроллим по фильтрам до кнопки 'Применить'")

    def click_filter_submit_button(self):
        self.get_filter_submit_button().click()
        print("Нажимаем кнопку 'Применить'")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Добавляем товар в корзину ('Купить')")

    def click_cart(self):
        self.get_cart().click()
        print("Нажимаем кнопку применить фильтр")

    # Methods

    def choosing_product(self):
        self.get_current_url()
        self.input_desired_item_name("rtx 4090")
        self.get_search_button()
        self.click_sorting_list()
        self.click_sorting_cheap_button()
        self.click_filter_manufacturer()
        self.scrolling_to_submit_button()
        self.click_filter_submit_button()
        self.assert_word(self.get_product_title(),
                         'Видеокарта ASUS GeForce RTX 4090 TUF Gaming OC Edition [TUF-RTX4090-O24G-GAMING] [PCI-E 4.0 24 ГБ GDDR6X, 384 бит, DisplayPort x3, HDMI x2, GPU 2230 МГц]')
        self.assert_price(self.get_price(), '248 999&nbsp;₽')
        self.click_add_to_cart_button()
        self.click_cart()


