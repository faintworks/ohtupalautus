*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Register Username  matti
    Set Register Password  Salasana123!
    Set Register Password Confirmation  Salasana123!
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Register Username  ma
    Set Register Password  Salasana123!
    Set Register Password Confirmation  Salasana123!
    Click Button  Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Register Username  matti
    Set Register Password  sa1
    Set Register Password Confirmation  sa1
    Click Button  Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Register Username  matti
    Set Register Password  salasanasana
    Set Register Password Confirmation  salasanasana
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Register Username  matti
    Set Register Password  Salasana123!
    Set Register Password Confirmation  Salasana456!
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Register Username  kalle
    Set Register Password  Salasana123!
    Set Register Password Confirmation  Salasana123!
    Click Button  Register
    Register Should Fail With Message  Username already exists


*** Keywords ***

Set Register Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Register Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Register Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
