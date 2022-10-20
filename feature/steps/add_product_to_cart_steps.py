from behave import when, then
from feature.page_objects.base_page import click_element_by_css_selector, wait_until_alert_is_present, accept_alert, get_element_text
from feature.page_objects.product_page import PRODUCT_CART_TITLE, SAMSUNG_GALAXY_S6_LINK, ADD_TO_CART_BTN, CART_LINK

@when('the user adds a product to cart')
def add_product_to_the_cart(context):
    click_element_by_css_selector(context, SAMSUNG_GALAXY_S6_LINK)
    click_element_by_css_selector(context, ADD_TO_CART_BTN)
    wait_until_alert_is_present(context)
    accept_alert(context)

@then('the product shows into cart')
def chek_cart(context):
    click_element_by_css_selector(context, CART_LINK)
    product_name = get_element_text(context, PRODUCT_CART_TITLE)
    assert product_name == 'Samsung galaxy s6'
