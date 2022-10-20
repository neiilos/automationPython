import os

from selenium import webdriver


def launch_browser(context, browser):
    cwd = os.getcwd()
    context.driver = webdriver.Chrome(
        executable_path=cwd + '\drivers\chromedriver.exe')
    context.driver.implicitly_wait(10)


def navigate_to_url(context, url):
    context.driver.get(url)
