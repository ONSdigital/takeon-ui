from selenium.webdriver.common.by import By

from base.driver_context import DriverContext
from base.selenium_core import SeleniumCore


class BasePage:

    def __init__(self, title):
        self.driver = DriverContext.driver
        self.check_page_title(title)

    HEADER_TITLE = By.XPATH, "//div[contains(@class,'header__title')]"

    def current_page_title(self):
        return SeleniumCore.find_elements_by(*BasePage.HEADER_TITLE)[0].text

    def check_page_title(self, page_title):
        current_title = self.current_page_title()
        if current_title.lower() != page_title.lower():
            assert False, 'Expected page header title to be "' + page_title + '" But the current page header title is "' + current_title + '"'
