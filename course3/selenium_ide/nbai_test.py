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
        self.driver = webdriver.Chrome("./../python_unit/chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://nbai.io/")
        # time.sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Sign up')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Sign Up')]").click()
        driver.find_element_by_xpath("//input[@id='firstName']").send_keys("charles")
        driver.find_element_by_xpath("//button[@id='m_login_signup_submit']").click()
        print(driver.find_element_by_xpath(
                '//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[2]/form/div[5]').text)
        try:
            self.assertEqual("This field is required.\nMinimum length of 6 including a letter and a number", driver.find_element_by_xpath(
                '//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[2]/form/div[5]').text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

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
