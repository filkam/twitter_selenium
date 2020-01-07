from webdrivermanager import GeckoDriverManager, ChromeDriverManager
from configparser import ConfigParser
from selenium import webdriver
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # serves to reference root path of the project for use in the fw
SETTINGS_PATH = os.path.join(ROOT_DIR, 'settings.ini')
cfg = ConfigParser()
cfg.read(SETTINGS_PATH)


# TODO specify webdriver installation path to be within the project and include binaries in .gitignore
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


def after_feature(context, feature):
    """ Defines actions to be taken after every feature """
    context.driver.quit()


# def take_screenshot(context):
#     """ Takes a screenshot of the rendered content and crops the image """
#     context.driver.save_screenshot("screenshot.png")  # TODO add formatting to filename
#     img = Image.open("screenshot.png")
#     cropped_filename = "/tmp/cropped-screenshot.png"
#     img.crop((0, 0, img.size[0], 400)).save(cropped_filename)
