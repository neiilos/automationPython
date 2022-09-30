from behave import when, then
from feature.page_objects.base_page import click_element_by_css_selector, send_keys_by_css_selector, wait_until_alert_is_present, get_alert_text, get_uuid4

UUID = get_uuid4()

@when('the user complete the Sign Up form')
def complete_sign_up_form(context):
    click_element_by_css_selector(context, '#signin2')
    send_keys_by_css_selector(context, '#sign-username', UUID)
    send_keys_by_css_selector(context, '#sign-password', UUID)
    click_element_by_css_selector(context, '#signInModal > div > div > div.modal-footer > button.btn.btn-primary')

@then('confirm message is displayed')
def alert_is_displayed(context):
    wait_until_alert_is_present(context)
    alert_text = get_alert_text(context)
    assert alert_text == 'Sign up successful.'

