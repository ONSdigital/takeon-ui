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
        if value_type == 'comment':
            self.submit_comment_value(value, question)
        elif value_type == 'total turnover':
            self.submit_total_turnover_value(value, question)
        elif value_type == 'internet sales':
            self.set_total_turnover_sales_value(value)

    def submit_comment_value(self, comment, question):
        SeleniumCore.switch_window()
        if comment.lower() == 'empty' or comment.lower() == 'blank':
            comment = ''
        if question.upper() == 'Q146':
            SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_NO_146, comment)

    def submit_total_turnover_value(self, value, question):
        SeleniumCore.switch_window()
        if value == 'blank':
            value = ''
        if question.upper() == 'Q20':
            SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_TURNOVER_ELEMENT, value)

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

    def submit_the_sales_values_for_survey(self, *questions):
        questions_list = questions[0]
        commodity_values = self.get_values_as_a_list(questions[1])
        SeleniumCore.switch_window()
        self.submit_the_commodity_values(questions_list, commodity_values)

    def submit_the_commodity_values(self, questions_list, values):
        if len(questions_list) == 5:
            question_codes = self.form_6_question_codes
        elif len(questions_list) == 6:
            question_codes = self.form_7_question_codes
        count = 0
        for value in values:
            count += 1
            question_element = question_codes.get(questions_list[count - 1])
            self.driver.find_element_by_id(question_element).clear()
            self.driver.find_element_by_id(question_element).send_keys(value)

    def get_values_as_a_list(self, values):
        new_values = values.split(',')
        commodity_values = []
        for new_val in new_values:
            commodity_values.append(new_val)
        return commodity_values
