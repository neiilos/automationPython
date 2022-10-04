Feature: Login to demoblaze

    As a common user
    I want to Login
    In order to have access to the application

    Scenario: Login with valid credentials
        Given the user is on demoblaze page
        When the user logs in with valid credentials
        Then home page is displayed
