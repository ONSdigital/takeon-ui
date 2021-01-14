from selenium.webdriver.common.by import By

from pages.common.base_page import BasePage

from base.selenium_core import SeleniumCore


class LoginPage(BasePage):

    def __init__(self):
        super().__init__('Login')

    USERNAME_FIELD = "signInFormUsername"
    PASSWORD_FIELD = "signInFormPassword"
    LOGIN_BUTTON = "signInSubmitButton"
    SIGN_OUT_BUTTON = ".btn--exit"

    def login(self, username, password):
        SeleniumCore.wait_for_element_to_be_displayed(By.ID, LoginPage.USERNAME_FIELD)
        self.driver.find_elements_by_id(LoginPage.USERNAME_FIELD)[1].send_keys(username)
        self.driver.find_elements_by_id(LoginPage.PASSWORD_FIELD)[1].send_keys(password)
        self.driver.find_elements_by_name(LoginPage.LOGIN_BUTTON)[1].click()

    def logout(self):
        sign_out_button = self.driver.find_element_by_css_selector(LoginPage.SIGN_OUT_BUTTON)
        if sign_out_button:
            sign_out_button.click()

    def check_page_title(self, page_title):
        pass