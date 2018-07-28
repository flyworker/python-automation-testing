import os.path
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WAITING_TIME = 5

class SampleLibrary(object):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self._sut_path = os.path.join(os.path.dirname(__file__),
                                      '..', 'sut', 'login.py')
        self._status = ''


    def open_browser(self, browser):
        self.driver = webdriver.Chrome('./robot_lib/chromedriver', chrome_options=self.options)
        self.driver.get(browser)
        assert "Facebook" in self.driver.title
        # assert "Log into Facebook" in driver.title


    def status_should_be(self, expected_status):
        assert expected_status in self.driver.find_element_by_xpath('//*[@id="header_block"]/span').text
        self.driver.close()