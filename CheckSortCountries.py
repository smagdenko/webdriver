from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin")


def login():

    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath(".//span[contains(.,'Countr')]").click()


def sorted_list():

    countries = driver.find_elements_by_xpath(".//*[@id='content']//tr//td[5]")
    ls=[]
    for country in countries:
        ls.append(country.text)
    sort_ls=sorted(ls)
    assert sort_ls == ls

def sorted_subcounteries():

    subcount = driver.find_elements_by_xpath(".//*[@id='table-zones']//tr//td[3] "
                                             "[.//*[not(contains(@type,'text'))]]")
    ls1 = []
    for sub in subcount:
        ls1.append(sub.text)
    sort_ls1 = sorted(ls1)
    assert sort_ls1 == ls1

def test_zones():

    login()
    sorted_list()
    zone = driver.find_elements_by_xpath(".//*[@id='content']//tr//td[6]")

    i = 0
    while i<len(zone):
        t = zone[i].get_attribute("textContent")
        i += 1

        if int(t)>0:
            driver.find_element_by_xpath(
                ".//*[@id='content']//td[6][contains(.," + t + ")]/preceding-sibling::td[1]/a").click()
            sorted_subcounteries()
            driver.back()
        zone = driver.find_elements_by_xpath(".//*[@id='content']//tr//td[6]")


