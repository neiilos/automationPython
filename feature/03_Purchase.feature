Feature: Purchase

    As a common user
    I want to buy a product
    In order to exercise a purchase

    Scenario: Successful purchase
        Given the user is on demoblaze page
        When the user buys a product
        Then confirmation message is displayed

    Scenario: Add product to cart
        Given the user is on demoblaze page
        When the user adds a product to card
        Then confirmation message is displayed

    Scenario: Navigate to cart
        Given the user is on demoblaze page
        When the user navigates to the cart
        Then cart page is displayed

    Scenario: Complete order form
        Given the user is on demoblaze page
        When the user navigates to the cart
        Then cart page is displayed