from behave import given, when, then
from pages import HomePage


def step_send_tweet(context, content):
    page = HomePage(context)
    page.tweet(content)
