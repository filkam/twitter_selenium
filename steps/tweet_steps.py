from behave import given, when, then
from pages import TwitterLoginPage


@given('user is on Twitter login page')
def step_open_login_page(context):
    page = TwitterLoginPage(context)
    page.load()


@when('user fills credentials in the form and submits')
def step_input_credentials_submit(context):
    pass