*** Settings ***
Library  OperatingSystem
Library  Selenium2Library
Resource  Selenium2Screenshots/keywords.robot

Suite Setup  Setup chromedriver
#Suite Teardown  Close all browsers

*** Keywords ***

Highlight heading
    [Arguments]  ${locator}
    Update element style  ${locator}  margin-top  0.75em
    Highlight  ${locator}

*** Test Cases ***

Take an annotated screenshot of RobotFramework.org
    Open browser  http://robotframework.org/
    Highlight heading  css=#header h1
    ${note1} =  Add pointy note
    ...    css=#header
    ...    This screenshot was generated using Robot Framework and Selenium.
    ...    width=250  position=bottom
    Capture and crop page screenshot  robotframework.png
    ...    header  ${note1}

*** Keywords ***

Setup chromedriver
  Set Environment Variable  webdriver.chrome.driver  ./robot_lib/chromedriver