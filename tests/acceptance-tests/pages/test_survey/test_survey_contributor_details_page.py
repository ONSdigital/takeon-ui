from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.check_contributor_details import CheckContributorDetails
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.common.contributor_details.submit_contributor_details import SubmitContributorDetails
from pages.locators import contributor_details


class TestSurveyContributorDetailsPage(SubmitContributorDetails):
    POPMRZ_QUESTION_PRIMARY_ELEMENT = '0023'
    POPMRZ_QUESTION_SECONDARY_ELEMENT = '0024'
    POPRRM_QUESTION_PRIMARY_ELEMENT = '0028'
    POPRRM_QUESTION_SECONDARY_ELEMENT = '0029'
    QUESTION_DERIVED_ELEMENT = '4001'
    COMMENT_QUESTION_NOT_BLANK = '5000'
    COMMENT_QUESTION_VALUE = '5001'
    THRESHOLD_PRIMARY_QUESTION_ELEMENT = '0011'
    THRESHOLD_DERIVED_QUESTION_ELEMENT = '0012'
    ERROR_MESSAGE_ELEMENT_STRING_PART_ONE = '//strong[contains(text(),"'
    ERROR_MESSAGE_ELEMENT_STRING_PART_TWO = '")]'
    TAB_ELEMENTS = By.XPATH, '//li[contains(@class,"tab__list-item tab__list-item--row")]'

    question_codes = {
        'Q1': '1000',
        'Q2': '1001'
    }

    def set_internet_sales_value(self, validation_type, value):
        if validation_type.lower() == 'poprrm':
            SeleniumCore.set_current_data_text(self.POPRRM_QUESTION_PRIMARY_ELEMENT, value)
        elif validation_type.lower() == 'popmrz':
            SeleniumCore.set_current_data_text(self.POPMRZ_QUESTION_PRIMARY_ELEMENT, value)

    def set_total_turnover_sales_value(self, validation_type, value):
        if validation_type.lower() == 'poprrm':
            SeleniumCore.set_current_data_text(self.POPRRM_QUESTION_SECONDARY_ELEMENT, value)
        elif validation_type.lower() == 'popmrz':
            SeleniumCore.set_current_data_text(self.POPMRZ_QUESTION_SECONDARY_ELEMENT, value)

    def submit_sales_values(self, validation_type, period_type, internet_sales, total_sales):
        if period_type == 'previous':
            self.submit_pp_sales_values(validation_type, internet_sales, total_sales)
        if period_type == 'current':
            self.submit_cp_sales_values(validation_type, internet_sales, total_sales)

    def submit_pp_sales_values(self, validation_type, internet_sales, total_sales):
        global pp_internet_sales, pp_total_sales
        pp_internet_sales = Utilities.convert_blank_data_value(internet_sales)
        pp_total_sales = Utilities.convert_blank_data_value(total_sales)
        self.set_internet_sales_value(validation_type, pp_internet_sales)
        self.set_total_turnover_sales_value(validation_type, pp_total_sales)
        CheckContributorDetails().save_the_application()
        SeleniumCore.close_the_current_window()

    def submit_cp_sales_values(self, validation_type, internet_sales, total_sales):
        global cp_internet_sales, cp_total_sales
        cp_internet_sales = Utilities.convert_blank_data_value(internet_sales)
        cp_total_sales = Utilities.convert_blank_data_value(total_sales)
        self.set_internet_sales_value(validation_type, cp_internet_sales)
        self.set_total_turnover_sales_value(validation_type, cp_total_sales)
        CheckContributorDetails().save_the_application()

    def validate_the_current_period_details(self, validation_type, internet_sales):
        self.set_internet_sales_value(validation_type, internet_sales)
        CheckContributorDetails().save_the_application()

    def run_the_validation_process(self, threshold_primary_value, exp_derived_value):
        SeleniumCore.set_current_data_text(self.THRESHOLD_PRIMARY_QUESTION_ELEMENT,
                                           threshold_primary_value)
        CheckContributorDetails().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(By.ID, self.THRESHOLD_DERIVED_QUESTION_ELEMENT)
        ReportingHelper.check_single_message_matches('Q12', actual_derived_val, exp_derived_value)

    def switch_to_the_tab(self, tab_name):
        elements = SeleniumCore.find_elements_by(*TestSurveyContributorDetailsPage.TAB_ELEMENTS)
        for ele in elements:
            if ele.text.lower() == tab_name.lower():
                ele.click()
                break

    def check_historic_data_back_periods(self, periods):
        table = self.driver.find_element_by_id("tabId2")
        rows = table.find_elements_by_tag_name("tr")
        periods = self.sort_periods_order(periods)
        for i in range(0, 1):
            cols = rows[i].find_elements_by_tag_name("th")
            count = 1
            for period in periods:
                ReportingHelper.check_single_message_matches('Question', cols[count].text, period)
                count += 1

    def sort_periods_order(self, periods):
        return sorted(periods, reverse=True)

    def check_pop_ratio_of_ratios_validation(self, factor_type,
                                             operator_type, threshold_value, result):
        CheckContributorDetails().check_if_overall_validation_triggered()
        is_validation_triggered = False
        if factor_type == 'increase':
            value_one = int(cp_internet_sales) * int(pp_total_sales)
            value_two = int(cp_total_sales) * int(pp_internet_sales)
            is_validation_triggered = ReportingHelper.compare_the_values_with_operator(operator_type, value_one,
                                                                                       int(threshold_value) * value_two)
        elif factor_type == 'decrease':
            value_one = int(cp_total_sales) * int(pp_internet_sales)
            value_two = int(cp_internet_sales) * int(pp_total_sales)
            is_validation_triggered = ReportingHelper.compare_the_values_with_operator(operator_type, value_one,
                                                                                       int(threshold_value) * value_two)
        elif factor_type == 'not-applicable':
            is_validation_triggered = 'false'

        ReportingHelper.check_single_message_matches('Q28', result, str(is_validation_triggered).lower())

    def check_historic_data_matches_with_current_period_data(self, survey, question_codes, values, tab_name):

        self.switch_to_the_tab(tab_name)
        if len(question_codes) > 1:
            values = Utilities.get_values_as_a_list(values)
            count = 0
            for value in values:
                question_row = GetContributorDetails().get_question_code_row_details('tabId2',
                                                                  Utilities.get_question_code_element(survey,
                                                                                                      question_codes[
                                                                                                          count]))
                elements = contributor_details.CURRENT_PERIOD_COLUMN
                current_period_value = question_row.find_elements(By.XPATH, elements)
                ReportingHelper.check_elements_message_matches(question_codes[count], current_period_value, value)
                count += 1
