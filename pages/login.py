from environment import SETTINGS_PATH
from configparser import ConfigParser


class TwitterLoginPage:
    cfg = ConfigParser()
    cfg.read(SETTINGS_PATH)
    USER = cfg['twitter.com']['Email']
    PASSWORD = cfg['twitter.com']['Password']
    URL = cfg['twitter.com']['Login_URL']

    def __init__(self, context):
        self.driver = context.driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, credentials):
        email_input_element = self.driver.find_element_by_css_selector("input.email-input")
        email_input_element.send_keys(self.USER)
        password_input_element = self.driver.find_element_by_css_selector(".LoginForm-password > input")
        password_input_element.send_keys(self.PASSWORD)
        email_input_element.submit()
