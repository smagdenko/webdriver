from selenium import webdriver

driver = webdriver.Chrome()


def find_element():

    driver.get("http://localhost/litecart/en/")
    duck_elements = driver.find_elements_by_xpath(".//*[contains(@class,'product')]//li")
    for elem in duck_elements:
        assert len(elem.find_elements_by_xpath(".//*[contains(@class,'sticker')]"))==1
    driver.close()

find_element()