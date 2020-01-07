

class Page:
    """ Generic Page class that contains basic actions applicable to all pages """

    def __init__(self, context):
        self.driver = context.driver

    def load(self, url):
        self.driver.get(url)