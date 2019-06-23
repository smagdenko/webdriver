from selenium import webdriver

driver = webdriver.Chrome()

def login():

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=2")

    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_open_page():

    login()
    items = driver.find_elements_by_xpath(".//*[@class='dataTable']//img/following-sibling::a")
    for item in range(len(items)):
        items[item].click()
        for l in driver.get_log("browser"):
            print(l)
        driver.back()
        items = driver.find_elements_by_xpath(".//*[@class='dataTable']//img/following-sibling::a")

