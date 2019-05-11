import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
WAITING_TIME = 5

class OrderLibrary(object):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    def user_enter_address_in_search_box(self, location):
        self.driver.get("https://www.skipthedishes.com/")
        print('Location', location)
        self.driver.find_element_by_name("address_display").click()
        self.driver.find_element_by_name("address_display").clear()
        self.driver.find_element_by_name("address_display").send_keys("Rue Sherbrooke Ouest, 666")
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="restaurant-search-form"]/div/div[1]/div/div[1]/div/div[1]/ul/li[1]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reset Pin'])[1]/following::button[1]").click()

    def chose_the_first_store_avaliable(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="restaurant-list-container"]/a[1]/div[4]/div/div[1]').click()

    def store_name_should_be(self,store_name):
        name=self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Close'])[2]/following::h1[1]").text
        if store_name != name:
            raise AssertionError("Expected status should be '%s' but was '%s'."
                                 % (store_name, name))
