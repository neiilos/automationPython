from behave import when, then 
from feature.page_objects.base_page import click_element_by_css_selector, wait_until_element_is_clickable, get_elements
from feature.page_objects.banner_page import CART_LINK
from feature.page_objects.cart_page import DELETE_CART_BTN, PRODUCT_CART_TITLE

@when ('the user deletes a product')
def delete_product_from_cart(context):
    click_element_by_css_selector(context, CART_LINK)
    wait_until_element_is_clickable(context, DELETE_CART_BTN)
    click_element_by_css_selector(context, DELETE_CART_BTN) 

@then ('the product is deleted')
def validate_product_deleted(context):
    elements = get_elements(context, PRODUCT_CART_TITLE)
    assert not elements