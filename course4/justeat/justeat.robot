*** Settings ***
Library           OperatingSystem
Library           justeat_lib/OrderLibrary.py
Library           SeleniumLibrary
Library           String
#Test Teardown  Close test browser
*** Variables ***
${ADDRESS}              Rue Sherbrooke Ouest, 666
${STORE_NAME}           Ta Pies (cuisine néo-zélandaise et australienne) 9.9

*** Test Cases ***
User can find a store close to the location
    [Tags]    UAT
    User Enter Address in Search Box    ${ADDRESS}
    Chose the first Store avaliable
    Store name should be    ${STORE_NAME}
#    Close all browsers