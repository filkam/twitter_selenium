from behave import given, when, then
from pages import HomePage, TweetPopup
from steps import login_steps


@Given('user is logged in')
def step_is_logged_in(context):
    login_steps.step_open_login_page(context)
    login_steps.step_input_credentials_submit(context)


@When('user clicks the tweet button')
def step_click_tweet_btn(context):
    page = HomePage(context)
    page.home_page_loaded()
    page.click_tweet_btn()


@When('user inputs the content into the text box')
def step_input_content_txt_box(context):
    popup = TweetPopup(context)
    assert popup.tweet_popup_present(), "Tweet popup did not appear"
    popup.input_tweet_content('falafelek')

@When('user clicks Tweet button')
def step_click_tweet(context):
    popup = TweetPopup(context)
    popup.click_to_tweet()

@Then('submitted tweet is published')
def step_tweet_is_published(context):
    page = HomePage(context)
    #page.click_profile()
    page.load(page.HOME_URL)
    page.home_page_loaded()
    assert page.tweet_on_page('falafelek')
