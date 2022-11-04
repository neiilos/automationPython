import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from uuid import uuid4


def click_element_by_css_selector(self, css_selector):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).click()


def send_keys_by_css_selector(self, css_selector, text):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)


def get_element_text(self, css_selector):
    return self.driver.find_element(By.CSS_SELECTOR, css_selector).text


def wait_until_element_displayed(self, css_selector):
    WebDriverWait(self.driver, 20).until(
        expected_conditions.visibility_of_element_located(css_selector)).text


def wait_until_element_is_clickable(self, css_selector):
    WebDriverWait(self.driver, 20).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))


def wait_until_text_is_present(self, css_selector, text):
    WebDriverWait(self.driver, 20).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), text))


def wait_until_alert_is_present(self):
    WebDriverWait(self.driver, 20).until(
        expected_conditions.alert_is_present())


def get_alert_text(self):
    return self.driver.switch_to.alert.text


def accept_alert(self):
    self.driver.switch_to.alert.accept()


def create_unique_user():
    return str(uuid.uuid4())


def get_elements(self, css_selector):
    self.driver.find_elements(By.CSS_SELECTOR, css_selector)