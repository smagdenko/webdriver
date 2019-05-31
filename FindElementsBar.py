from selenium import webdriver

driver = webdriver.Chrome()


def find_element_bar():

    driver.get("http://localhost/litecart/admin")

    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath(".//span[contains(.,'Appearence')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Appearence')]//..//..//span[contains(.,'Template')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Appearence')]//..//..//span[contains(.,'Logotype')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Catalog')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Product')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Option')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Manufacturers')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Suppliers')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Delivery')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Sold Out')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Quantity')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'CSV')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Catalog')]//..//../ul//span[contains(.,'Suppliers')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Countries')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Currencies')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Customers')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Customers')]//..//../ul//span[contains(.,'Customers')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Customers')]//..//../ul//span[contains(.,'CSV')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Customers')]//..//../ul//span[contains(.,'Newsletter')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Geo Zones')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Geo Zones')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Languages')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Languages')]//..//../ul//span[contains(.,'Storage Encoding')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Modules')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()



    driver.find_element_by_xpath(".//span[contains(.,'Modules')]//..//../ul//span[contains(.,'Customer')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Modules')]//..//../ul//span[contains(.,'Shipping')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Modules')]//..//../ul//span[contains(.,'Payment')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Modules')]//..//../ul//span[contains(.,'Total')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Modules')]//..//../ul//span[contains(.,'Success')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Modules')]//..//../ul//span[contains(.,'Action')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Orders')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Languages')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Orders')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Orders')]//..//../ul//span[contains(.,'Statuses')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Pages')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Languages')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Languages')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Reports')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()



    driver.find_element_by_xpath(".//span[contains(.,'Slides')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Tax')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Tax')]//..//../ul//span[contains(.,'Rates')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'Defaults')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'General')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'Listings')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'Images')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'Checkout')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'Advanced')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Settings')]//..//../ul//span[contains(.,'Security')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Translation')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Translation')]//..//../ul//span[contains(.,'Scan')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Translation')]//..//../ul//span[contains(.,'CSV')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'Users')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()

    driver.find_element_by_xpath(".//span[contains(.,'vQmods')]").click()
    title = driver.find_element_by_xpath(".//h1")
    assert title.is_displayed()


    print("pass")

    driver.close()

find_element_bar()