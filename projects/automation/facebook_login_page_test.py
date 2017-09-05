from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome('./chromedriver',chrome_options=options)

driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()
