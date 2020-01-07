from pages.page import Page


class HomePage(Page):
    """Page object for twitter.com home page (after log in)"""

    def __init__(self, driver):
        super().__init__(driver)

    def tweet(self, content):
        element = self.context.driver.find_element_by_id('tweet-box-home-timeline')
        element.send_keys(content)
        self.context.driver.find_element_by_css_selector('button.tweet-action').click()

