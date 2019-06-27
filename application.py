from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from selenium import webdriver


class Applications:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = self.driver.get("http://litecart.stqa.ru/en/")
        self.base_page = BasePage(self)
        self.item_page = ItemPage(self)
        self.basket_page = BasketPage(self)



