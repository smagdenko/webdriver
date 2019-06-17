from selenium import webdriver

driver = webdriver.Chrome()


def login():

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_sort():

    login()
    countries = driver.find_elements_by_xpath(".//*[@class='dataTable']//td[3]/a")

    for i in range(len(countries)):
        len(countries)
        countries[i].click()
        # zones = driver.find_elements_by_xpath(".//*[@class='dataTable']"
        #                                       "//td[3]//select[contains(@name,'zones')]")

        select = driver.find_elements_by_xpath(".//select[contains(@name, 'zones[1][zone_code]')]/option[@value !='']")
        ls = []
        for element in select:
            ls.append(element.text)
        ls1 = sorted(ls)
        assert ls1 == ls
        driver.back()
        countries = driver.find_elements_by_xpath(".//*[@class='dataTable']//td[3]/a")