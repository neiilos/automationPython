from behave import given, when, then
from feature.page_objects.base_page import click_element_by_css_selector, send_keys_by_css_selector, wait_until_alert_is_present, get_alert_text, create_unique_user
from feature.utils.common_constants import VALID_PASSWORD, VALID_USERNAME
from feature.page_objects.home_page import MODAL_SIGNUP_BTN, PASSWORD_FIELD_MODAL_SIGNUP, USERNAME_FIELD_MODAL_SIGNUP, LOGIN_URL, MODAL_LOGIN_BTN, USERNAME_FIELD_MODAL_LOGIN, PASSWORD_FIELD_MODAL_LOGIN
from feature.page_objects.banner_page import SIGNUP_BTN, LOGIN_BTN, LOGOUT_BTN
from utils.driver import launch_browser
from feature.page_objects.base_page import send_keys_by_css_selector, click_element_by_css_selector, get_element_text, wait_until_text_is_present

@given('the user is on demoblaze page')
def navigate_to_demoblaze(context):
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)

@when('the user logs in with valid credentials')
def login_with_valid_credentials(context):
    click_element_by_css_selector(context, LOGIN_BTN)
    send_keys_by_css_selector(
        context, USERNAME_FIELD_MODAL_LOGIN, VALID_USERNAME)
    send_keys_by_css_selector(
        context, PASSWORD_FIELD_MODAL_LOGIN, VALID_PASSWORD)
    click_element_by_css_selector(context, MODAL_LOGIN_BTN)

@when('the user creates an account')
def complete_sign_up_form(context):
    click_element_by_css_selector(context, SIGNUP_BTN)
    UUID = create_unique_user()
    send_keys_by_css_selector(context, USERNAME_FIELD_MODAL_SIGNUP, UUID)
    send_keys_by_css_selector(
        context, PASSWORD_FIELD_MODAL_SIGNUP, VALID_PASSWORD)
    click_element_by_css_selector(context, MODAL_SIGNUP_BTN)

@then('home page is displayed')
def user_is_redirected_to_home_page(context):
    wait_until_text_is_present(context, LOGOUT_BTN, 'Log out')
    log_out_btn = get_element_text(context, LOGOUT_BTN)
    assert log_out_btn == 'Log out'

@then('confirmation message is displayed')
def alert_is_displayed(context):
    wait_until_alert_is_present(context)
    alert_text = get_alert_text(context)
    assert alert_text == 'Sign up successful.'