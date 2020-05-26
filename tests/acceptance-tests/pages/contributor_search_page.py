from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage


class ContributorSearchPage(BasePage):
    REFERENCE_TEXT_FIELD = By.ID, 'reference'
    PERIOD_TEXT_FIELD = By.ID, 'period'
    SURVEY_TEXT_FIELD = By.ID, 'survey'
    SEARCH_BUTTON = By.XPATH, "//button[@class='btn btn--small']"

    def select_the_reference_view_form(self, survey, reference, period):
        self.submit_search_details(survey, reference, period)
        table = self.driver.find_element_by_id("ResultsTable")
        rows = table.find_elements_by_tag_name("tr")
        # Ignore the first row
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see if any references appear that shouldn't be there
            if (cols[i].text == reference and cols[i + 1].text == period):
                cols[i - 1].click()
                break

    def submit_search_details(self, survey, reference, period):
        ele = SeleniumCore.set_element_text(*ContributorSearchPage.REFERENCE_TEXT_FIELD, reference)
        # ele.send_keys(reference)
        ele = SeleniumCore.set_element_text(*ContributorSearchPage.PERIOD_TEXT_FIELD,period)
        # ele.send_keys(period)
        ele = SeleniumCore.set_element_text(*ContributorSearchPage.SURVEY_TEXT_FIELD,survey)
        # ele.send_keys(survey)
        self.driver.find_element(*ContributorSearchPage.SEARCH_BUTTON).click()
