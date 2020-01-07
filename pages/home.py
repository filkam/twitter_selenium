from pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class HomePage(Page):
    """Page object for twitter.com home page (after log in)"""
    HOME_URL = "https://twitter.com/home"

    def __init__(self, driver):
        super().__init__(driver)

    def click_tweet_btn(self):
        btn = self.driver.find_element_by_css_selector('a.r-urgr8i')
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.r-urgr8i')))
            btn.click()
        except TimeoutException:
            raise

    def home_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.css-901oao > span:nth-child(1)')))
            return True
        except TimeoutException:
            return False

    def click_profile(self):
        profile_link = self.driver.find_element_by_css_selector('a.css-4rbku5:nth-child(7) > div:nth-child(1)')
        profile_link.click()

    def tweet_on_page(self, content):
        self.click_profile()
        try:
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.r-1ljd8xs'), content))
            return True
        except TimeoutException:
            raise


class TweetPopup(HomePage):
    """ Page object handling the new tweet popup window """

    def __init__(self, driver):
        super().__init__(driver)

    def tweet_popup_present(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-1dqxon3 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')))
            return True
        except TimeoutException:
            return False

    def input_tweet_content(self, content):
        txt_box = self.driver.find_element_by_css_selector('.r-1dqxon3 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        txt_box.send_keys(content)

    def click_to_tweet(self):
        btn = self.driver.find_element_by_css_selector('div.r-urgr8i:nth-child(4)')
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.r-urgr8i:nth-child(4)')))
            btn.click()
        except TimeoutException:
            raise
