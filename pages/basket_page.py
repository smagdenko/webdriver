from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage:

    def __init__(self, app):
        self.app = app

    def remove_items_from_table(self):

        driver = self.app.driver
        table = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']//td[@class='item']")
        for _ in table:
            get_item_text = driver.find_element_by_xpath(".//*[@value='Remove']//../preceding-sibling::p/a").get_attribute("textContent")
            items_from_table = driver.find_element_by_xpath("//div[@id='order_confirmation-wrapper']//tr/td[text()='%s']" % get_item_text)
            driver.find_element_by_xpath("//a[contains(.,'%s')]//../following-sibling::p/button[@value='Remove']" % get_item_text).click()
            wait = WebDriverWait(driver, 10)
            wait.until(lambda _: EC.invisibility_of_element_located(
                (By.XPATH, "//div[@id='order_confirmation-wrapper']//tr/td[text()='%s']" % items_from_table)))
            driver.refresh()

    def check_message(self):

        driver = self.app.driver
        message = driver.find_element_by_xpath(".//*[@id='checkout-cart-wrapper']//em[contains(.,'no items')]")
        assert message.is_displayed()