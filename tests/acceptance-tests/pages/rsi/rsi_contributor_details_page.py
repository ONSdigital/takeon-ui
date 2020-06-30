from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from pages.common.contributor_details_page import ContributorDetailsPage


class RsiContributorDetailsPage(ContributorDetailsPage):
    QUESTION_TOTAL_TURNOVER_ELEMENT = By.ID, '0020'
    QUESTION_TWO_ELEMENT = By.ID, '0021'
    QUESTION_NO_146 = By.ID, '0146'
    QUESTION_TURNOVER_ELEMENT = By.ID, '0020'
    QUESTION_LABEL_PART_ONE = "//label[contains(text(),'"
    QUESTION_LABEL_PART_TWO = "')]"
    QUESTION_DERIVED_ELEMENT = By.ID, '7034'

    form_6_question_codes = {
        'Q22': '0022',
        'Q23': '0023',
        'Q24': '0024',
        'Q25': '0025',
        'Q26': '0026',
    }

    form_7_question_codes = {
        'Q22': '0022',
        'Q23': '0023',
        'Q24': '0024',
        'Q25': '0025',
        'Q26': '0026',
        'Q27': '0027',
    }

    def set_internet_sales_value(self, value):
        SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_TWO_ELEMENT, value)

    def set_total_turnover_sales_value(self, value):
        SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_TOTAL_TURNOVER_ELEMENT, value)

    def submit_pp_sales_values(self, internet_sales, total_sales):
        SeleniumCore.switch_window()
        self.pp_internet_sales = internet_sales
        self.pp_total_sales = total_sales
        self.set_internet_sales_value(internet_sales)
        self.set_total_turnover_sales_value(total_sales)
        ContributorDetailsPage().save_the_application()
        SeleniumCore.close_the_current_window()

    def submit_question_value(self, value_type, value, question):
        SeleniumCore.switch_window()
        if value_type:
            self.submit_sales_value(value, question)

    def submit_sales_value(self, value, question):
        if value.lower() == 'blank':
            value = ''
            SeleniumCore.set_element_text_by_id(self.get_question_code_element(question), value)

    def validate_the_current_period_details(self, internet_sales):
        SeleniumCore.switch_window()
        self.set_internet_sales_value(internet_sales)
        ContributorDetailsPage().save_the_application()

    def check_threshold_value(self):
        if int(self.pp_internet_sales) > 0.1 * int(self.pp_total_sales):
            return False

    def check_validation_message(self):
        exp_msg = "This value is 0. Previous period it was more than a certain percentage of the total."
        actual_msg = ContributorDetailsPage().get_validation_error_message('Q21')
        if exp_msg == actual_msg:
            return True
        else:
            return False

    def check_comment_present_val_msg(self, exp_msg, is_val_exists):
        ContributorDetailsPage().check_validation_message('Q146', exp_msg, is_val_exists)

    def get_derived_question_value(self):
        return int(SeleniumCore.get_attribute_element_text(*RsiContributorDetailsPage.QUESTION_DERIVED_ELEMENT))

    def run_the_validation_process(self, total_turnover_value, exp_derived_value):
        SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_TOTAL_TURNOVER_ELEMENT, total_turnover_value)
        ContributorDetailsPage().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(
            *RsiContributorDetailsPage.QUESTION_DERIVED_ELEMENT)
        ReportingHelper.check_single_message_matches('Q7034', actual_derived_val, exp_derived_value)
