*** Settings ***
Library           OperatingSystem
Library           robot_lib/LoginLibrary.py
Library           SeleniumLibrary
Library           String

Force Tags        facebook

*** Variables ***
${USERNAME}               janedoe
${PASSWORD}               J4n3D0e
${NEW PASSWORD}           e0D3n4J
${DATABASE FILE}          ${TEMPDIR}${/}robotframework-quickstart-db.txt
${PWD INVALID LENGTH}     Password must be 7-12 characters long
${NO APLE GET}     No apple get
${PWD INVALID CONTENT}    Password must be a combination of lowercase and uppercase letters and numbers

*** Test Cases ***
User cannot log in with bad password
    [Tags]    UAT
    ${RANDOM_STRING}=    Generate Random String    5
    Attempt to Login with Credentials   ${RANDOM_STRING}      ${PASSWORD}
    Status Should Be    Log into Facebook


User can create an account and log in
    [Tags]    UAT
    ${RANDOM_USERNAME}=    Generate Random String    5
    Create Valid User    ${RANDOM_USERNAME}    ${PASSWORD}
    Log    Create Valid User ${RANDOM_USERNAME}
    Attempt to Login with Credentials    ${RANDOM_USERNAME}    ${PASSWORD}
    Status Should Be    Logged In

For-Loop-In-Range
    [Tags]    Functional Test
    : FOR    ${INDEX}    IN RANGE    1    3
    \    Log    ${INDEX}
    \    ${RANDOM_STRING}=    Generate Random String    ${INDEX}
    \    Log    first ${RANDOM_STRING}
For-Loop-Elements
    [Tags]    Functional Test
    @{ITEMS}    Create List    Star Trek    Star Wars    Perry Rhodan
    :FOR    ${ELEMENT}    IN    @{ITEMS}
    \    Log    ${ELEMENT}
    \    ${ELEMENT}    Replace String    ${ELEMENT}    ${SPACE}    ${EMPTY}
    \    Log    ${ELEMENT}

For-Loop-Exiting
    [Tags]    Functional Test
    @{ITEMS}    Create List    Good Element 1    Break On Me    Good Element 2
    :FOR    ${ELEMENT}    IN    @{ITEMS}
    \    Log    ${ELEMENT}
    \    Run Keyword If    '${ELEMENT}' == 'Break On Me'    Exit For Loop
    \    Log    Do more actions here ...

*** Keywords ***
Clear login database
    Remove file    ${DATABASE FILE}

Create valid user
    [Arguments]    ${username}    ${password}
    Create user    ${username}    ${password}
#    Status should be    SUCCESS

Creating user with invalid password should fail
    [Arguments]    ${password}    ${error}
    Create user    example    ${password}
    Status should be    Creating user failed: ${error}

Login
    [Arguments]    ${username}    ${password}
    Attempt to login with credentials    ${username}    ${password}
    Status should be    Logged In

Database Should Contain
    [Arguments]    ${username}    ${password}    ${status}
    ${database} =     Get File    ${DATABASE FILE}
    Should Contain    ${database}    ${username}\t${password}\t${status}\n

A user has a valid account
    Create valid user    ${USERNAME}    ${PASSWORD}

She changes her password
    Change password    ${USERNAME}    ${PASSWORD}    ${NEW PASSWORD}
    Status should be    SUCCESS

She can log in with the new password
    Login    ${USERNAME}    ${NEW PASSWORD}

She cannot use the old password anymore
    Attempt to login with credentials    ${USERNAME}    ${PASSWORD}
    Status should be    Access Denied

