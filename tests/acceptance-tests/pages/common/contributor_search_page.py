import time

from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from pages.common.base_page import BasePage


class ContributorSearchPage(BasePage):
    REFERENCE_TEXT_FIELD = 'reference'
    PERIOD_TEXT_FIELD = 'period'
    SURVEY_TEXT_FIELD = 'survey'
    SEARCH_BUTTON = By.XPATH, "//button[@class='btn btn--small']"
    NEXT_BUTTON = By.ID, 'next_button'

    def select_the_reference_view_form(self, survey, reference, period, sic_code):
        self.submit_search_details(reference, period, survey)
        self.select_the_form_row(reference, period, sic_code)

    def select_the_form_row(self, reference, period, sic_code):
        table = SeleniumCore.wait_for_element_to_be_displayed(By.ID, "ResultsTable")
        rows = table.find_elements_by_tag_name("tr")
        # Ignore the first row
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see the sic code exists
            if sic_code:
                ReportingHelper.check_single_message_matches(reference, cols[i + 6].text, sic_code)
            # Check to see if any references appear that shouldn't be there
            if (cols[1].text == reference and cols[2].text == period):
                cols[0].click()
                break

    def get_all_the_periods(self, reference, period, sic_code):
        self.no_of_periods = []
        period_details = self.get_the_no_of_periods(self.no_of_periods)
        self.no_of_periods = period_details[1]
        # elements = SeleniumCore.find_elements_by(*ContributorSearchPage.NEXT_BUTTON)
        while SeleniumCore.find_elements_by(*ContributorSearchPage.NEXT_BUTTON)[0].is_displayed():
            SeleniumCore.find_elements_by(*ContributorSearchPage.NEXT_BUTTON)[0].click()
            time.sleep(2)
            period_details = self.get_the_no_of_periods(self.no_of_periods)
            self.no_of_periods = period_details[1]
        self.select_the_form_row(reference, period, sic_code)
        return self.no_of_periods

    def get_the_no_of_periods(self, periods):
        table = SeleniumCore.wait_for_element_to_be_displayed(By.ID, "ResultsTable")
        # table = self.driver.find_element_by_id("ResultsTable")
        rows = table.find_elements_by_tag_name("tr")
        count = len(rows)
        # self.periods = []
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see if any references appear that shouldn't be there
            periods.append(cols[2].text)
            count -= 1
        return count, periods

    def submit_search_details(self, *search_types):
        reference = search_types[0]
        period = search_types[1]
        survey = search_types[2]
        if reference == 'empty':
            reference = ''
        elif period == 'empty':
            period = ''
        elif survey == 'empty':
            survey = ''
        SeleniumCore.set_element_text(self.REFERENCE_TEXT_FIELD, reference)
        SeleniumCore.set_element_text(self.PERIOD_TEXT_FIELD, period)
        SeleniumCore.set_element_text(self.SURVEY_TEXT_FIELD, survey)
        self.driver.find_element(*ContributorSearchPage.SEARCH_BUTTON).click()
