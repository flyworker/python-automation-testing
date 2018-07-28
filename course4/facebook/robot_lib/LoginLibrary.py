import os.path
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
WAITING_TIME = 5

class LoginLibrary(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__),
                                      '..', 'sut', 'login.py')
        self._status = ''

    def create_user(self, username, password):
        self._run_command('create', username, password)

    def change_password(self, username, old_pwd, new_pwd):
        self._run_command('change-password', username, old_pwd, new_pwd)

    def attempt_to_login_with_credentials(self, username, password):
        # super().__init__()


        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome('./robot_lib/chromedriver', chrome_options=options)
        self.driver.get("http://www.facebook.com")

        assert "Facebook" in self.driver.title

        self.driver.implicitly_wait(WAITING_TIME)
        elem = self.driver.find_element_by_id("email")
        elem.send_keys(username)
        elem = self.driver.find_element_by_id("pass")

        elem.send_keys(password)

        self.driver.implicitly_wait(WAITING_TIME)

        elem.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(WAITING_TIME)

    def status_should_be(self, expected_status):
        header= self.driver.find_element_by_xpath('//*[@id="header_block"]/span').text

        if expected_status != header:
            raise AssertionError("Expected status should be '%s' but was '%s'."
                                 % (expected_status, header))

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()
