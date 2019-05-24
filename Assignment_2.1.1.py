from selenium import webdriver

driver = webdriver.Chrome()

def find_element():

    driver.get("https://www.keepsolid.com")
    driver.close()

find_element()
