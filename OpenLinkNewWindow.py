from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
addr = driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

def login():

    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

def test_open_new_windows():

    login()
    edit_icon = driver.find_element_by_xpath(".//a[contains(@href,'AF')]//../i[@class='fa fa-pencil']").click()
    edit_links = driver.find_elements_by_xpath(".//i[@class='fa fa-external-link']")

    for link in edit_links:

        wait = WebDriverWait(driver, 10)
        original_window = driver.current_window_handle
        old_windows = driver.window_handles

        link.click()
        wait.until(EC.new_window_is_opened(old_windows))
        # wait.until(EC.number_of_windows_to_be(2))
        new_window = [elem for elem in driver.window_handles if elem not in old_windows]
        driver.switch_to.window(new_window[0])
        driver.close()
        driver.switch_to_window(original_window)
