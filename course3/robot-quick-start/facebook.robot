*** Settings ***
Library           lib/FacebookLibrary.py
*** Test Cases ***

#User cannot log in with bad password
#    Create Valid User    betty    P4ssw0rd
#    Attempt to Login with Credentials    betty    wrong
#    Status Should Be    Access Denied


User cannot log in with bad password
    Attempt to Login with Credentials    betty    wrong
    Status Should Be    Log into Facebook

*** Keywords ***



