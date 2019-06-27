from selenium import webdriver

class BasePage:

    def __init__(self, app):
        self.app = app

    def checkout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[contains(.,'Checkout')]").click()
        return self

    def add_item(self):
        driver = self.app.driver
        driver.find_element_by_xpath(".//*[@id='box-most-popular']//li[1]").click()

    def back_driver(self):
        driver = self.app.driver
        driver.back()

    def refresh(self):
        driver = self.app.driver
        driver.refresh()
