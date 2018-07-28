*** Settings ***
Library           OperatingSystem
Library           robot_lib/LoginLibrary.py
Library           Selenium2Screenshots

Force Tags        quickstart
Default Tags      example    smoke

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
    Attempt to Login with Credentials    betty    wrong
    Status Should Be    Log Into Facebook

*** Keywords ***
Clear login database
    Remove file    ${DATABASE FILE}

Create valid user
    [Arguments]    ${username}    ${password}
    Create user    ${username}    ${password}
    Status should be    SUCCESS

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

