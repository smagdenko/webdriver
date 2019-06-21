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

        select = driver.find_elements_by_xpath("//form[contains(@method,'post')]//td[3]//option[@selected='selected']")
        ls_countries = []
        for element in select:
            ls_countries.append(element.text)
        sorted_countries = sorted(ls_countries)
        assert sorted_countries == ls_countries
        driver.back()
        countries = driver.find_elements_by_xpath(".//*[@class='dataTable']//td[3]/a")
