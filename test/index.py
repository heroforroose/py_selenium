from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
elem = browser.find_element_by_id("kw")
elem.send_keys("python" + Keys.RETURN)
browser.quit()