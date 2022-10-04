from behave import given, when, then
from utils.driver import launch_browser
from feature.page_objects.login_page import LOGIN_URL, LOGIN_BTN, MODAL_LOGIN_BTN, USERNAME_FIELD_MODAL_LOGIN, PASSWORD_FIELD_MODAL_LOGIN
from feature.utils.common_constants import VALID_PASSWORD, VALID_USERNAME
from feature.page_objects.base_page import send_keys_by_css_selector, click_element_by_css_selector, get_element_text, wait_until_element_is_clickable, wait_until_text_is_present

@given ('the user is on demoblaze page')
def navigate_to_demoblaze(context):
    launch_browser(context,'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)

@when ('the user logs in with valid credentials')
def login_with_valid_credentials(context) :
    click_element_by_css_selector(context, LOGIN_BTN)
    send_keys_by_css_selector(context, USERNAME_FIELD_MODAL_LOGIN, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD_MODAL_LOGIN, VALID_PASSWORD)
    click_element_by_css_selector(context, MODAL_LOGIN_BTN)

@then ('home page is displayed')
def user_is_redirected_to_home_page(context):
    wait_until_text_is_present(context,'#logout2', 'Log out')
    log_out_btn = get_element_text(context, '#logout2')
    assert log_out_btn == 'Log out'
    
