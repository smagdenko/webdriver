from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class ItemPage:

    def __init__(self, app):
        self.app = app

    # def add_to_cart(self):
    #     self.app.driver.find_element_by_xpath("//*[@name='add_cart_product']").click()


    def add_to_cart(self):

        driver = self.app.driver
        # driver.find_element_by_xpath("//*[@name='add_cart_product']").click()
        if len(driver.find_elements_by_xpath(".//select[@name='options[Size]']")) > 0:
            size_element = driver.find_element_by_xpath(".//select[@name='options[Size]']/option[@value='Medium']")
            size_element.click()
            add_to_cart_button = driver.find_element_by_xpath(".//*[@name='add_cart_product']")
            add_to_cart_button.click()
        else:
            driver.find_element_by_xpath(".//*[@name='add_cart_product']").click()

    def get_text_element(self):
        driver = self.app.driver
        text_elem = driver.find_element_by_xpath(".//span[@class='quantity']").text
        wait = WebDriverWait(driver, 10)
        wait.until(lambda _: int(driver.find_element_by_xpath(".//span[@class='quantity']").text) == int(text_elem) + 1)


