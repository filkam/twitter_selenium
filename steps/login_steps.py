from behave import given, when, then
from pages import LoginPage, HomePage

URL = LoginPage.LOGIN_URL


@given('non-logged user is on Twitter login page')
def step_open_login_page(context):
    page = LoginPage(context)
    page.load(URL)


@when('user fills credentials "{email}" "{password}" in the form and submits')
def step_input_credentials_submit(context, email, password):
    page = LoginPage(context)
    page.login(email, password)


@then('user is logged in and can see the Home page')
def step_logged_in(context):
    page = HomePage(context)
    assert page.home_page_loaded(), "Page did not load correctly."
