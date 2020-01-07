from webdrivermanager import GeckoDriverManager, ChromeDriverManager
from configparser import ConfigParser
from selenium import webdriver
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(ROOT_DIR, 'settings.ini')
cfg = ConfigParser()
cfg.read(SETTINGS_PATH)


def get_driver():
    browser = cfg['meta']['Browser']

    if browser.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().download_and_install()[0])
    elif browser.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().download_and_install()[0])
    return driver


def before_feature(context, feature):
    context.driver = get_driver()
    #context.driver.implicitly_wait(cfg['meta']['ImplicitlyWait'])


def after_feature(context, feature):
    context.driver.quit()
