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
                SeleniumCore.check_multiple_windows_exists(cols[0])
                break

    def get_all_the_periods(self, reference, period, sic_code):
        self.periods = []
        self.periods = self.get_no_of_periods(self.periods)
        # Check if next button displayed then go to next page to get remaining periods
        while SeleniumCore.find_elements_by(*ContributorSearchPage.NEXT_BUTTON)[0].is_displayed():
            SeleniumCore.find_elements_by(*ContributorSearchPage.NEXT_BUTTON)[0].click()
            time.sleep(2)
            self.periods = self.get_no_of_periods(self.periods)
        self.select_the_form_row(reference, period, sic_code)
        return self.periods

    def get_no_of_periods(self, periods):
        table = SeleniumCore.wait_for_element_to_be_displayed(By.ID, "ResultsTable")
        rows = table.find_elements_by_tag_name("tr")
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            periods.append(cols[2].text)
        return periods

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
