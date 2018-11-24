# -*- coding: utf-8 -*-
import os
import platform

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
        print(platform.system())
        if platform.system() == "Windows":
            self.driver = webdriver.Chrome("./../driver/chromedriver.exe")
        else:
            self.driver = webdriver.Chrome("./../driver/chromedriver")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get(
            "https://www.iga.net/en/online_grocery?gclid=EAIaIQobChMIg8KK9d7t3gIVzv_jBx0GoA7GEAAYASAAEgJvl_D_BwE")
        driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").click()
        driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").clear()
        driver.find_element_by_xpath('//a[contains(text(),"OK")]').click()
        time.sleep(1)
        driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").send_keys("coffee")

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header_0_SearchBox_BtnSearch"]/span[1]').click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='+'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(
            '//*[@id="MyStoreSidebar_Screen1Panel"]/div[3]/div[2]/div[2]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="header_0_MobileCartLink"]/span').click()
        time.sleep(2)
        try:
            self.assertEqual("$17.19", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Estimated total'])[1]/following::div[1]").text)
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
