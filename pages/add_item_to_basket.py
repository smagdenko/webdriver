from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
addr = driver.get("http://litecart.stqa.ru/en/")


def test_add_item_to_cart():
    for i in range(3):
        driver.find_element_by_xpath(".//*[@id='box-most-popular']//li[1]").click()
        if len(driver.find_elements_by_xpath(".//select[@name='options[Size]']")) > 0:
            driver.find_element_by_xpath(".//select[@name='options[Size]']/option[@value='Medium']").click()
            add_to_cart_button = driver.find_element_by_xpath(".//*[@name='add_cart_product']")
            add_to_cart_button.click()
        else:
            driver.find_element_by_xpath(".//*[@name='add_cart_product']").click()

        text_elem = driver.find_element_by_xpath(".//span[@class='quantity']").text
        wait = WebDriverWait(driver, 10)
        wait.until(lambda _: int(driver.find_element_by_xpath(".//span[@class='quantity']").text) == int(text_elem) + 1)
        driver.back()

    driver.find_element_by_xpath(".//a[contains(.,'Checkout')]").click()
    table = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']//td[@class='item']")
    for _ in table:
        duck = driver.find_element_by_xpath(".//*[@value='Remove']//../preceding-sibling::p/a").get_attribute(
            "textContent")
        # ducks = driver.find_element_by_xpath("//div[@id='order_confirmation-wrapper']//tr/td[text()='%s']" % duck)
        driver.find_element_by_xpath(
            "//a[contains(.,'%s')]//../following-sibling::p/button[@value='Remove']" % duck).click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda _: EC.invisibility_of_element_located(
            (By.XPATH, "//div[@id='order_confirmation-wrapper']//tr/td[text()='%s']" % duck)))
        driver.refresh()
