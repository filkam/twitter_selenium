from pages.page import Page


class LoginPage(Page):
    """Page object for Twitter.com login page"""
    LOGIN_URL = "https://twitter.com/login"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, user, password):
        """ Handles user login action using specified credentials """
        email_input_element = self.driver.find_element_by_css_selector(".js-username-field")
        email_input_element.send_keys(user)
        password_input_element = self.driver.find_element_by_css_selector(".js-password-field")
        password_input_element.send_keys(password)
        self.driver.find_element_by_css_selector("button.submit").click()

    def is_login_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.signin - wrapper')))
            return True
        except TimeoutException:
            return False
