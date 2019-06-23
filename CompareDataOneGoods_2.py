from selenium import webdriver
import re

driver = webdriver.Chrome()


def login():
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_open_page():

    driver.get("http://localhost/litecart/en/")

    name = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//div[@class='name']").get_attribute("textContent")
    regular_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//*[contains(@class,'regular')]").value_of_css_property("color")
    size_reg_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//*[contains(@class,'regular')]").value_of_css_property("font-size")
    color_reg_price = re.findall(r'\d{1,3}',regular_price)
    promo_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//strong").value_of_css_property("color")
    size_promo_price = driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]//strong").value_of_css_property("font-size")

    driver.find_element_by_xpath(".//*[@id='box-campaigns']//a[1]").click()

    compare_name = driver.find_element_by_xpath(".//*[@itemprop='name']").get_property("textContent")
    compare_reg_price = driver.find_element_by_xpath(".//*[@class='regular-price']").value_of_css_property("color")
    compare_promo_price = driver.find_element_by_xpath(".//*[@class='price-wrapper']//strong").value_of_css_property("color")
    rgb_reg_price = re.findall(r'\d{1,3}',compare_promo_price)

    red_color = [int(l) for l in rgb_reg_price[:3]]
    red_color = sum(red_color[1:])

    grey_color = [int(l) for l in color_reg_price[:3]]
    elem_grey_color = sum(grey_color)//len(grey_color)


    assert red_color == 0, str(red_color)
    assert elem_grey_color == grey_color[0], str(grey_color)
    assert name == compare_name
    assert size_promo_price != size_reg_price
    driver.close()