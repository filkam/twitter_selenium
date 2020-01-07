from webdrivermanager import GeckoDriverManager, ChromeDriverManager
from configparser import ConfigParser
from selenium import webdriver
import os
from allure_behave.hooks import allure_report
import random
import string

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # serves to reference root path of the project for use in the fw
SETTINGS_PATH = os.path.join(ROOT_DIR, 'settings.ini')
allure_report(os.path.join(ROOT_DIR, 'reports/'))

cfg = ConfigParser()
cfg.read(SETTINGS_PATH)


def get_driver():
    """ Handles download and installation of a required webdriver according to parameters set in settings.ini """
    browser = cfg['meta']['Browser']

    if browser.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().download_and_install()[0])
    elif browser.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().download_and_install()[0])
    return driver


def before_feature(context, feature):
    """ Defines actions to be taken before every feature """
    context.driver = get_driver()
    context.driver.implicitly_wait(cfg['meta']['ImplicitWait'])
    context.driver.maximize_window()


def after_feature(context, feature):
    """ Defines actions to be taken after every feature """
    context.driver.quit()


def generate_random_string():
    """ Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(70))
