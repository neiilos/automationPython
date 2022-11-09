from behave import when, then
from feature.page_objects.base_page import click_element_by_css_selector, wait_until_element_is_clickable, get_elements, get_element_text
from feature.page_objects.banner_page import CART_LINK
from feature.page_objects.cart_page import DELETE_CART_BTN, FIRST_PRODUCT_CART_TITLE, SECOND_PRODUCT_CART_TITLE


@when('the user deletes a product')
def delete_product_from_cart(context):
    click_element_by_css_selector(context, CART_LINK)
    wait_until_element_is_clickable(context, DELETE_CART_BTN)
    click_element_by_css_selector(context, DELETE_CART_BTN)


@then('the product shows into cart')
def chek_cart(context):
    click_element_by_css_selector(context, CART_LINK)
    product_name = get_element_text(context, FIRST_PRODUCT_CART_TITLE)
    assert product_name == 'Samsung galaxy s6'


@then('the product is deleted')
def validate_product_deleted(context):
    elements = get_elements(context, FIRST_PRODUCT_CART_TITLE)
    assert not elements


@then('the products shows into cart')
def chek_cart_with_same_product_twice(context):
    click_element_by_css_selector(context, CART_LINK)
    product_one_name = get_element_text(context, FIRST_PRODUCT_CART_TITLE)
    product_two_name = get_element_text(context, SECOND_PRODUCT_CART_TITLE)
    assert product_one_name == 'Samsung galaxy s6'
    assert product_two_name == 'Samsung galaxy s6'
