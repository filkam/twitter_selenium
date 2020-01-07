from behave import given, when, then
from pages import TwitterLoginPage, HomePage
from environment import SETTINGS_PATH
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read(SETTINGS_PATH)
USER = cfg['twitter.com']['Email']
PASSWORD = cfg['twitter.com']['Password']
URL = cfg['twitter.com']['Login_URL']


@given('user is on Twitter login page')
def step_open_login_page(context):
    page = TwitterLoginPage(context)
    page.load(URL)


@when('user fills credentials in the form and submits')
def step_input_credentials_submit(context):
    page = TwitterLoginPage(context)
    page.login(USER, PASSWORD)


@then('user is logged in and can see the Home page')
def step_logged_in(context):
    pass



