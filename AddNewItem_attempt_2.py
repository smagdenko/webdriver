from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random

driver = webdriver.Chrome()

addition = random.randint(0, 10)
name = "testname"+ str(addition)
code = "12345"

def login():

    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

def change_path_dirrectory():
    file = "selen.png"
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    return config_file


def add_new_item():

    login()
    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]").click()
    driver.find_element_by_xpath(".//*[@class='button'][contains(.,'Product')]").click()

    driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[1]/td/label[1]/input").click()

    driver.find_element_by_xpath(".//span[@class='input-wrapper']//input").send_keys(name)
    driver.find_element_by_xpath(".//*[@name='code']").send_keys(code)
    upload = driver.find_element_by_xpath(".//input[@type='file']")
    upload.send_keys(change_path_dirrectory())
    information()
    price()

    assertion_name = driver.find_elements_by_xpath(".//table[@class='dataTable']//tr//a")
    for i in assertion_name:
        if i.text == name:
            print(i.text)
    # assert name == assertion_name

def information():

    inf = driver.find_element_by_xpath("//a[contains(.,'Information')]").click()
    driver.find_element_by_xpath(".//select[@name='manufacturer_id']//option[@value='1']").click()
    driver.find_element_by_xpath(".//input[contains(@name,'short_description')]").send_keys("short")
    driver.find_element_by_xpath(".//input[contains(@name,'head_title')]").send_keys("head")
    driver.find_element_by_xpath(".//input[contains(@name,'meta')]").send_keys("meta")

def price():

    driver.find_element_by_xpath("//a[contains(.,'Prices')]").click()
    driver.find_element_by_xpath(".//input[contains(@name,'purchase_price')]").send_keys("25")
    driver.find_element_by_xpath(".//select[contains(@name,'currency')]//option[@value='USD']").click()
    driver.find_element_by_xpath(".//input[@name='prices[USD]']").send_keys("50")
    driver.find_element_by_xpath(".//*[@id='content']/form/p/span/button[1]").click()

add_new_item()
