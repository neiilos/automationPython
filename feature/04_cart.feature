Feature: cart

    As a common user
    I want to navigate to cart
    In order to check the products

    Scenario: Add product to cart
        Given the user is on demoblaze page
        When the user adds a product to cart
        Then the product shows into cart

    Scenario: Add more than one product to cart
        Given the user is on demoblaze page
        When the user adds two times the same product to cart
        Then the products shows into cart

    Scenario: Delete a product
        Given the user has a product on cart
        When the user deletes a product
        Then the product is deleted
