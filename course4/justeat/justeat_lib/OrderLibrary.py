import time
from robot.api import logger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
WAITING_TIME = 5

class OrderLibrary(object):
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    def user_enter_address_in_search_box(self, location):
        self.driver.get("https://www.skipthedishes.com/")
        logger.console("Hello world!")

        self.driver.find_element_by_xpath('//input').click()

        self.driver.find_element_by_xpath('//input').send_keys("666 Rue Sherbrooke Ouest")
        self.driver.find_element_by_xpath("//p/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div[1]/div/div[1]/div[1]/div/div/div/div/button').click()
        # logger.console("Hello world2!")
        # for element in self.driver.find_elements_by_xpath('//div[@data-cy="RestaurantRow"]/a/div/div/div[1]/div[2]/div/div'):
        #     logger.console(element.text)

    def chose_the_first_store_avaliable(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div[1]/div/div/div/div[4]/div/div/div/div[1]/a/div/div[2]').click()


    def store_name_should_be(self,store_name):
        time.sleep(2)
        name=self.driver.find_element_by_xpath("//h1").text
        if store_name != name:
            raise AssertionError("Expected status should be '%s' but was '%s'."
                                 % (store_name, name))
