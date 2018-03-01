*** Settings ***
Library           lib/FacebookLibrary.py
Resource  Selenium2Screenshots/keywords.robot
*** Test Cases ***

User cannot log in with bad password
    Attempt to Login with Credentials    betty    wrong
    Status Should Be    Log into Facebook
    Capture and crop page screenshot  login_page.png
*** Keywords ***



