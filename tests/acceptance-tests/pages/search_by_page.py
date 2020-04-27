from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchByPage(BasePage):
    REFERENCE = By.NAME, 'reference'
    PERIOD = By.NAME, 'period'
    SURVEY = By.NAME, 'survey'
    SEARCH_BUTTON = By.XPATH, "//button[@class='btn btn--small']"

    def select_search_by(self, reference_number):
        self.select_search_by_options()
        # ele = self.driver.find_element(*SearchByPage.REFERENCE)
        # ele.send_keys(reference_number)
        # elem = self.driver.find_element(*SearchByPage.SEARCH_BUTTON)
        # elem.click()

    def select_search_by_options(self):
        self.is_checked(*SearchByPage.REFERENCE)
        self.is_checked(*SearchByPage.PERIOD)
        self.is_checked(*SearchByPage.SURVEY)
        elem = self.driver.find_element(*SearchByPage.SEARCH_BUTTON)
        elem.click()

    def is_checked(self, *element):
        element_to_be_checked = self.driver.find_element(*element)
        if element_to_be_checked.get_attribute("checked") == "false":
            self.driver.find_element(element_to_be_checked).click()
