# -*- coding: utf-8 -*-
from selenium import webdriver
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
        self.base_url = "https://www.just-eat.ca/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver

        driver.get(self.base_url)
        driver.find_element_by_xpath('//*[@id="mm-modal"]/div/button').click()
        time.sleep(2)
        driver.find_element_by_id("homepage-search-fullAddress").send_keys(
            "Rue Sherbrooke Ouest, 666, H3A 1E4, Montréal")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='skipToMain']/div[2]/div/div/button/span").click()
        driver.find_element_by_xpath(
            '//*[@id="searchResults"]/div/div[1]/section[1]/a/div[2]/div/div[1]/header/h3').click()

        self.assertEqual("Pizza Italia (St. Laurent)", driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Pizza Italia (St Laurent)'])[1]/following::h1[1]").text)

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
