from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.check_contributor_details import CheckContributorDetails
from pages.common.contributor_details.submit_contributor_details import SubmitContributorDetails


class RsiContributorDetailsPage(SubmitContributorDetails):
    QUESTION_TOTAL_TURNOVER_ELEMENT = '20'
    QUESTION_INTERNET_SALES_ELEMENT = '21'
    QUESTION_LABEL_PART_ONE = "//label[contains(text(),'"
    QUESTION_LABEL_PART_TWO = "')]"
    QUESTION_DERIVED_ELEMENT = By.ID, '7034'

    def set_internet_sales_value(self, value):
        SeleniumCore.set_current_data_text(self.QUESTION_INTERNET_SALES_ELEMENT, value)

    def set_total_turnover_sales_value(self, value):
        SeleniumCore.set_current_data_text(self.QUESTION_TOTAL_TURNOVER_ELEMENT, value)

    def submit_sales_values(self, period_type, internet_sales, total_sales):
        if period_type == 'previous':
            self.submit_pp_sales_values(internet_sales, total_sales)
        if period_type == 'current':
            self.submit_cp_sales_values(internet_sales, total_sales)

    def submit_pp_sales_values(self, internet_sales, total_sales):
        global pp_internet_sales, pp_total_sales
        pp_internet_sales = Utilities.convert_blank_data_value(internet_sales)
        pp_total_sales = Utilities.convert_blank_data_value(total_sales)
        self.set_internet_sales_value(pp_internet_sales)
        self.set_total_turnover_sales_value(pp_total_sales)
        CheckContributorDetails().save_the_application()
        SeleniumCore.close_the_current_window()

    def submit_cp_sales_values(self, internet_sales, total_sales):
        global cp_internet_sales, cp_total_sales
        cp_internet_sales = Utilities.convert_blank_data_value(internet_sales)
        cp_total_sales = Utilities.convert_blank_data_value(total_sales)
        self.set_internet_sales_value(cp_internet_sales)
        self.set_total_turnover_sales_value(cp_total_sales)
        CheckContributorDetails().save_the_application()

    def validate_the_current_period_internet_sales_details(self, internet_sales):
        self.set_internet_sales_value(internet_sales)
        CheckContributorDetails().save_the_application()

    def validate_the_current_period_details(self, internet_sales, total_sales):
        self.set_internet_sales_value(internet_sales)
        self.set_total_turnover_sales_value(total_sales)
        CheckContributorDetails().save_the_application()

    def get_derived_question_value(self):
        return int(SeleniumCore.get_attribute_element_text(*RsiContributorDetailsPage.QUESTION_DERIVED_ELEMENT))

    def run_the_validation_process(self, total_turnover_value, exp_derived_value):
        SeleniumCore.set_current_data_text(self.QUESTION_TOTAL_TURNOVER_ELEMENT,
                                           total_turnover_value)
        CheckContributorDetails().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(
            *RsiContributorDetailsPage.QUESTION_DERIVED_ELEMENT)
        ReportingHelper.check_single_message_matches('Q7034', actual_derived_val, exp_derived_value)

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

        ReportingHelper.check_single_message_matches('Q21', result, str(is_validation_triggered).lower())
