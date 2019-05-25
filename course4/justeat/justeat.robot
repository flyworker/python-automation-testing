*** Settings ***
Library           OperatingSystem
Library           justeat_lib/OrderLibrary.py
Library           Selenium2Library
Library           String
Library           Selenium2Screenshots
Test Teardown  Close Browser
*** Variables ***
${ADDRESS}              Rue Sherbrooke Ouest, 666
${STORE_NAME}           Restaurant Nouilles Épicées Express

*** Test Cases ***
User can find a store close to the location
    [Tags]    UAT
    User Enter Address in Search Box    ${ADDRESS}
    Chose the first Store avaliable
    Store name should be    ${STORE_NAME}
    Close Browser