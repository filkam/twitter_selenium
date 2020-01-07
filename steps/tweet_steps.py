from behave import given, when, then
from pages import HomePage, TweetPopup, LoginPage
from steps import login_steps
from configparser import ConfigParser
from environment import SETTINGS_PATH, generate_random_string

cfg = ConfigParser()
cfg.read(SETTINGS_PATH)
EMAIL = cfg['default_user']['Email']
PASSWORD = cfg['default_user']['Password']

content = generate_random_string()


@Given('user is logged in as a default user')
def step_is_logged_in(context):
    login_steps.step_open_login_page(context)
    page = LoginPage(context)
    if page.is_login_page:
        login_steps.step_input_credentials_submit(context, EMAIL, PASSWORD)


@When('user clicks the tweet button')
def step_click_tweet_btn(context):
    page = HomePage(context)
    page.home_page_loaded()
    page.click_tweet_btn()


@When('user inputs content into the text box')
def step_input_content_txt_box(context):
    popup = TweetPopup(context)
    assert popup.tweet_popup_present(), "Tweet popup did not appear"
    popup.input_tweet_content(content)


@When('user clicks Tweet button')
def step_click_tweet(context):
    popup = TweetPopup(context)
    popup.click_to_tweet()


@Then('submitted tweet is published')
def step_tweet_is_published(context):
    page = HomePage(context)
    page.load(page.HOME_URL)
    page.home_page_loaded()
    assert page.tweet_on_page(content)
