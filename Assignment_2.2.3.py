from selenium import webdriver

driver = webdriver.Chrome("insert a path to the driver")

def login():
    driver.get("http://localhost/litecart")

    driver.find_element_by_name("email").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.close()

login()

