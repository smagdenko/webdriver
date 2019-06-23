from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
addr = driver.get("http://litecart.stqa.ru/en/")


def test_add_item_to_cart():

    for i in range(5):
        driver.find_element_by_xpath(".//*[@id='box-most-popular']//li[1]").click()
        if len(driver.find_elements_by_xpath(".//select[@name='options[Size]']")) > 0:
            driver.find_element_by_xpath(".//select[@name='options[Size]']/option[@value='Medium']").click()
            add_to_cart_button = driver.find_element_by_xpath(".//*[@name='add_cart_product']").click()
        else:
            driver.find_element_by_xpath(".//*[@name='add_cart_product']").click()

        elem = driver.find_element_by_xpath(".//span[@class='quantity']").text
        time.sleep(1)
        elem1 = driver.find_element_by_xpath(".//span[@class='quantity']").text
        if elem == elem1: pass
        driver.back()

    driver.find_element_by_xpath(".//a[contains(.,'Checkout')]").click()
    table = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']//td[@class='item']")
    while len(table) > 0:
        duck = driver.find_element_by_xpath(".//*[@value='Remove']//../preceding-sibling::p/a").get_attribute(
            "textContent")
        ducks = driver.find_element_by_xpath("//div[@id='order_confirmation-wrapper']//tr/td[text()='%s']" % duck)
        remove_button = driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//*[@value='Remove']").click()
        # wait = WebDriverWait(driver, 5)
        # wait.until(lambda wd: EC.staleness_of(ducks))
        time.sleep(1)
        table = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']//td[@class='item']")
