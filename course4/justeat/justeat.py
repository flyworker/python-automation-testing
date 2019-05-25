# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.skipthedishes.com/")

        driver.find_element_by_xpath('//input').click()

        driver.find_element_by_xpath('//input').send_keys("666 Rue Sherbrooke Ouest")
        driver.find_element_by_xpath("//p/span").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div[1]/div/div[1]/div[1]/div/div/div/div/button').click()

        for element in driver.find_elements_by_xpath('//div[@data-cy="RestaurantRow"]/a/div/div/div[1]/div[2]/div/div'):
            print(element.text)

        driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div[1]/div/div/div/div[4]/div/div/div/div[1]/a/div/div[2]').click()


        driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[14]/div/div/div[2]/div[1]/div/div[1]/div[1]/h3').click()
        driver.find_element_by_xpath('//button/span[1]/div/div[2]').click()
        time.sleep(3)
        # Add 2nd product
        # parent_h = driver.current_window_handle
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[14]/div/div/div[2]/div[3]/div/div[1]/div[1]/h3/span').click()
        time.sleep(3)


        # driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/div[1]/div[3]/h6').click()
        driver.find_element_by_xpath('//button/span[1]/div/div[2]').click()
        #
        # driver.execute_script("window.scrollTo(550,300)")
        mainmenu = driver.find_element_by_xpath(
            '/html/body/div[10]/div[2]/div[2]/div[2]/div[1]/div[2]/ul/div[1]/div/div[1]')
        action = ActionChains(driver)
        action.move_to_element(mainmenu).perform()
        time.sleep(3)
        mainmenu.click()

        driver.find_element_by_xpath('//button/span[1]/div/div[2]').click()
        # do stuff in the popup
        # popup window closes
        # driver.switch_to.window(parent_h)
        item1_amount=float(driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/h3/span").text[1:])
        item2_amount=float(driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/h3/span").text[1:])
        total_amount=float(driver.find_element_by_xpath(
            "//span[contains(.,'$9.49')]").text[1:])
        self.assertEqual(item1_amount+item2_amount,total_amount+0.01)
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
