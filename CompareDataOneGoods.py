from selenium import webdriver

driver = webdriver.Chrome()


def login():
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_open_page():

    driver.get("http://localhost/litecart/en/")

    name = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//div[@class='name']").get_attribute("textContent")
    regular_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//*[contains(@class,'regular')]").value_of_css_property("color")
    reg_price_size = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//*[contains(@class,'regular')]").value_of_css_property("font-size")
    promo_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//strong").value_of_css_property("color")
    promo_price_size = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//strong").value_of_css_property("font-size")

    driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]").click()

    compare_name = driver.find_element_by_xpath(".//*[@itemprop='name']").get_property("textContent")
    compare_reg_price = driver.find_element_by_xpath(".//*[@class='price-wrapper']//s").value_of_css_property("color")
    compare_promo_price = driver.find_element_by_xpath(".//*[@class='price-wrapper']//strong").value_of_css_property("color")

    try:
        assert name == compare_name
        assert promo_price == compare_promo_price
        assert regular_price == compare_reg_price
        assert promo_price_size != reg_price_size
    except AssertionError as e:
        print("ERROR", e)
    finally:
        driver.close()