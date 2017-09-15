
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = "ecv"
pwd = "12345"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome('./chromedriver',chrome_options=options)

driver.get("http://www.facebook.com")

assert "Facebook" in driver.title
time.sleep(3)
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
time.sleep(5)
elem.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
