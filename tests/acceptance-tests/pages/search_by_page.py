from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchByPage(BasePage):
    REFERENCE = By.ID, 'reference'
    PERIOD = By.NAME, 'period'
    SURVEY = By.NAME, 'survey'
    SEARCH_BUTTON = By.XPATH, "//button[@class='btn btn--small']"

    def select_search_by(self, reference_number):
        ele = self.driver.find_element(*SearchByPage.REFERENCE)
        ele.send_keys(reference_number)
        elem = self.driver.find_element(*SearchByPage.SEARCH_BUTTON)
        elem.click()
