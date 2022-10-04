Feature: Create an account

    As a common user
    I want to Create an account
    In order to have an user account

    Scenario: Create an account
        Given the user is on demoblaze page
        When the user creates an account
        Then confirmation message is displayed
    