from behave import when, then
from feature.page_objects.base_page import click_element_by_css_selector, send_keys_by_css_selector, wait_until_alert_is_present, get_alert_text, create_unique_user
from feature.utils.common_constants import VALID_PASSWORD
from feature.page_objects.create_account_page import SIGNUP_BTN, MODAL_SIGNUP_BTN, PASSWORD_FIELD_MODAL_SIGNUP, USERNAME_FIELD_MODAL_SIGNUP


@when('the user creates an account')
def complete_sign_up_form(context):
    click_element_by_css_selector(context, SIGNUP_BTN)
    UUID = create_unique_user()
    send_keys_by_css_selector(context, USERNAME_FIELD_MODAL_SIGNUP, UUID)
    send_keys_by_css_selector(
        context, PASSWORD_FIELD_MODAL_SIGNUP, VALID_PASSWORD)
    click_element_by_css_selector(context, MODAL_SIGNUP_BTN)


@then('confirmation message is displayed')
def alert_is_displayed(context):
    wait_until_alert_is_present(context)
    alert_text = get_alert_text(context)
    assert alert_text == 'Sign up successful.'
