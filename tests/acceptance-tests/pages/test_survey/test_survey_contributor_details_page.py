from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from pages.common.base_page import BasePage
from pages.common.contributor_details_page import ContributorDetailsPage


class TestSurveyContributorDetailsPage(BasePage):
    QUESTION_ONE_ELEMENT = '1000'
    QUESTION_TWO_ELEMENT = '1001'
    QUESTION_DERIVED_ELEMENT = '4001'
    COMMENT_QUESTION_NOT_BLANK = '5000'
    COMMENT_QUESTION_VALUE = '5001'
    ERROR_MESSAGE_ELEMENT_STRING_PART_ONE = '//strong[contains(text(),"'
    ERROR_MESSAGE_ELEMENT_STRING_PART_TWO = '")]'
    QUESTION_LABEL_PART_ONE = "//label[contains(text(),'"
    QUESTION_LABEL_PART_TWO = "')]"

    question_codes = {
        'Q1': '1000',
        'Q2': '1001'
    }

    def set_internet_sales_value(self, value):
        SeleniumCore.set_element_text(self.QUESTION_TWO_ELEMENT, value)

    def set_total_turnover_sales_value(self, value):
        SeleniumCore.set_element_text(self.QUESTION_ONE_ELEMENT, value)

    def submit_pp_sales_values(self, internet_sales, total_sales):
        SeleniumCore.switch_window()
        self.pp_internet_sales = internet_sales
        self.pp_total_sales = total_sales
        self.set_internet_sales_value(internet_sales)
        self.set_total_turnover_sales_value(total_sales)
        ContributorDetailsPage().save_the_application()
        SeleniumCore.close_the_current_window()

    def validate_the_current_period_details(self, internet_sales):
        SeleniumCore.switch_window()
        self.set_internet_sales_value(internet_sales)
        ContributorDetailsPage().save_the_application()

    def run_the_validation_process(self, exp_derived_value):
        ContributorDetailsPage().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(
            *TestSurveyContributorDetailsPage.QUESTION_DERIVED_ELEMENT)
        ReportingHelper.check_single_message_matches('Q6', actual_derived_val, exp_derived_value)

    def get_derived_question_value(self):
        return int(SeleniumCore.get_attribute_element_text(*TestSurveyContributorDetailsPage.QUESTION_DERIVED_ELEMENT))

    def check_threshold_value(self):
        if int(self.pp_internet_sales) > 0.1 * int(self.pp_total_sales):
            return False

    def check_validation_message(self):
        element_text = "This value is 0. Previous period it was more than a certain percentage of the total."
        element = self.ERROR_MESSAGE_ELEMENT_STRING_PART_ONE + element_text + self.ERROR_MESSAGE_ELEMENT_STRING_PART_TWO
        if len(self.driver.find_elements_by_xpath(element)) > 0:
            return True
        else:
            return False

    def submit_question_value(self, value_type, value, question):
        SeleniumCore.switch_window()
        if value_type == 'value':
            pass
        elif value_type == 'comment':
            self.submit_comment_value(value, question)

    def submit_comment_value(self, comment, question):
        if comment.lower() == 'empty' or comment.lower() == 'blank':
            comment = ''
        if question.upper() == 'Q7':
            SeleniumCore.set_element_text(self.COMMENT_QUESTION_NOT_BLANK, comment)
        if question.upper() == 'Q8':
            SeleniumCore.set_element_text(self.COMMENT_QUESTION_VALUE, comment)

    def submit_the_sales_values_for_survey(self, *questions):
        questions_list = questions[0]
        commodity_values = self.get_values_as_a_list(questions[1])
        SeleniumCore.switch_window()
        self.submit_the_commodity_values(questions_list, commodity_values)

    def submit_the_commodity_values(self, questions_list, values):
        count = 0
        for value in values:
            count += 1
            question_element = self.question_codes.get(questions_list[count - 1])
            self.driver.find_element_by_id(question_element).clear()
            self.driver.find_element_by_id(question_element).send_keys(value)

    def get_values_as_a_list(self, values):
        new_values = values.split(',')
        commodity_values = []
        for new_val in new_values:
            commodity_values.append(new_val)
        return commodity_values
