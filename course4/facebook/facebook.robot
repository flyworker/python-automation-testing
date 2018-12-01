*** Settings ***
Library           OperatingSystem
Library           robot_lib/LoginLibrary.py
Library           SeleniumLibrary
Library           String

Force Tags        facebook

*** Variables ***
${USERNAME}               janedoe
${PASSWORD}               J4n3D0e

*** Test Cases ***
User cannot log in with bad password
    [Tags]    UAT
    ${RANDOM_STRING}=    Generate Random String    5
    Attempt to Login with Credentials   ${RANDOM_STRING}      ${PASSWORD}
    Status Should Be    Log Into Facebook


User can create an account and log in
    [Tags]    UAT
    ${RANDOM_USERNAME}=    Generate Random String    5
    Create Valid User    ${RANDOM_USERNAME}    ${PASSWORD}
    Log    Create Valid User ${RANDOM_USERNAME}
    Attempt to Login with Credentials    ${RANDOM_USERNAME}    ${PASSWORD}
    Status Should Be    Logged In

*** Keywords ***

Create valid user
    [Arguments]    ${username}    ${password}
    Create user    ${username}    ${password}
#    Status should be    SUCCESS
