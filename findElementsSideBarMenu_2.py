from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost/litecart/admin")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

def search_names():
    
    titles = driver.find_elements_by_xpath(".//*[@id='app-']/a/span[2]")

    i=0
    while i< len(titles):
        titles[i].click()
        i+=1

        subtitles = driver.find_elements_by_xpath(".//ul[contains(@class, 'docs')]//li")
        if len(subtitles)>0:
            j=0
            while j<len(subtitles):
                subtitles[j].click()
                j+=1
                assert driver.find_element_by_xpath(".//h1").is_displayed()
                subtitles = driver.find_elements_by_xpath(".//ul[contains(@class, 'docs')]//li")
        else:
            assert driver.find_element_by_xpath(".//h1").is_displayed()
        titles = driver.find_elements_by_xpath(".//*[@id='app-']/a/span[2]")

    driver.close()

search_names()