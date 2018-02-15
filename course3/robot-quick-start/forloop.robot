*** Settings ***
Library           String

*** Test Cases ***
For-Loop-In-Range
    : FOR    ${INDEX}    IN RANGE    1    3
    \    Log    ${INDEX}
    \    ${RANDOM_STRING}=    Generate Random String    ${INDEX}
    \    Log    ${RANDOM_STRING}

For-Loop-Elements
    @{ITEMS}    Create List    Star Trek    Star Wars    Perry Rhodan
    :FOR    ${ELEMENT}    IN    @{ITEMS}
    \    Log    ${ELEMENT}
    \    ${ELEMENT}    Replace String    ${ELEMENT}    ${SPACE}    ${EMPTY}
    \    Log    ${ELEMENT}

For-Loop-Exiting
    @{ITEMS}    Create List    Good Element 1    Break On Me    Good Element 2
    :FOR    ${ELEMENT}    IN    @{ITEMS}
    \    Log    ${ELEMENT}
    \    Run Keyword If    '${ELEMENT}' == 'Break On Me'    Exit For Loop
    \    Log    Do more actions here ...

Repeat-Action
    Repeat Keyword    2    Log    Repeating this ...