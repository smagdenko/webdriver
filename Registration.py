from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Chrome()
driver.get("http://litecart.stqa.ru/en/")

r = random.randint(0,100)
add_mail = str(r)
eml = "tst" + add_mail + "@test.com"
passw = "11111111"

def login():

    driver.find_element_by_xpath(".//*[@id='navigation']//input[@name='email']").send_keys(eml)
    driver.find_element_by_xpath(".//*[@id='navigation']//input[@name='password']").send_keys(passw)
    driver.find_element_by_xpath(".//*[@id='navigation']//*[@name='login']").click()

def logout():
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(".//*[@class='content']//a[contains(@href,'logout')]").click()

def test_registration():

    driver.find_element_by_xpath(".//*[@id='navigation']//*[contains(@href,'account')]").click()

    country = Select(driver.find_element_by_xpath(".//td[contains(.,'Country')]//select"))
    taxId = driver.find_element_by_xpath(".//input[contains(@name,'tax_id')]")
    company = driver.find_element_by_xpath(".//input[contains(@name,'company')]")
    first_name = driver.find_element_by_xpath(".//input[contains(@name,'first')]")
    lastName = driver.find_element_by_xpath(".//input[contains(@name,'last')]")
    address_1 = driver.find_element_by_xpath(".//input[contains(@name,'address1')]")
    postcode = driver.find_element_by_xpath(".//input[contains(@name,'postcode')]")
    city = driver.find_element_by_xpath(".//input[contains(@name,'city')]")
    email = driver.find_element_by_xpath(".//input[contains(@name,'email')]")
    phone = driver.find_element_by_xpath(".//input[contains(@name,'phone')]")
    password = driver.find_element_by_xpath(".//input[contains(@name,'passw')]")
    conf_password = driver.find_element_by_xpath(".//input[contains(@name,'confirmed_password')]")
    subm_button = driver.find_element_by_xpath(".//*[contains(@type,'submit')]")


    country.select_by_value("US")
    taxId.send_keys("Test taxId")
    company.send_keys("my Company")
    first_name.send_keys("Sergey")
    lastName.send_keys("Lastname")
    address_1.send_keys("Street")
    postcode.send_keys("12345")
    city.send_keys("Odessa")
    email.send_keys(eml)
    phone.clear()
    phone.send_keys("+380931478523")
    password.send_keys(passw)
    conf_password.send_keys(passw)
    subm_button.click()

    logout()
    login()
    logout()

    driver.close()

