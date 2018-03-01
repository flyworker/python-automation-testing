from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WAITING_TIME = 5


def login_fail_test(driver, user, pwd):
    assert "Facebook" in driver.title

    driver.implicitly_wait(WAITING_TIME)
    elem = driver.find_element_by_id("email")
    elem.send_keys(user)
    elem = driver.find_element_by_id("pass")

    elem.send_keys(pwd)

    driver.implicitly_wait(WAITING_TIME)

    elem.send_keys(Keys.RETURN)

    driver.implicitly_wait(WAITING_TIME)
    # assert "Log into Facebook" in driver.title
    assert "Log into Facebook" in driver.find_element_by_xpath('//*[@id="header_block"]/span').text


if __name__ == "__main__":
    user = "ecv"
    pwd = "12345"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    driver.get("http://www.facebook.com")

    login_fail_test(driver, user, pwd)

    driver.close()
