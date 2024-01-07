from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_Page
from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.payment_page import Payment_Page


def test_buy_product(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\checa\\PycharmProjects\\pythonProject\\oop\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.choosing_product()

    cp = Cart_Page(driver, mp)
    cp.click_checkout_button()

    p = Payment_Page(driver)
    p.select_product()

    driver.quit()
