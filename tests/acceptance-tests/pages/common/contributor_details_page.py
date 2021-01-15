import time
from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from common.override_messages import OverrideMessages
from common.validation_messages import ValidationMessages
from pages.common.base_page import BasePage
from pages.locators import contributor_details


class ContributorDetailsPage(BasePage):

    def __init__(self):
        if self.current_page_title() == 'Search':
            SeleniumCore.switch_window()
        super().__init__('Data Clearing')

    def get_no_of_validation_error_messages_per_question(self, question):
        self.override_the_validation(question, 'validation')
        question_row = self.get_question_code_row_details(contributor_details.CURRENT_DATA_TAB_ELEMENT, question)
        elements = contributor_details.ERROR_MESSAGES_COLUMN + contributor_details.ERROR_MESSAGES_ELEMENT
        return question_row.find_elements(By.XPATH, elements)

    def override_the_validation(self, question, type_of_check):
        question_row = self.get_question_code_row_details(contributor_details.CURRENT_DATA_TAB_ELEMENT, question)
        check_boxes = question_row.find_elements_by_name(contributor_details.OVERRIDE_CHECKBOX_ELEMENT)
        count = 0
        for i in range(0, len(check_boxes)):
            if type_of_check == 'validation' and check_boxes[i].get_attribute("checked") == "true" or \
                    type_of_check == 'override' and check_boxes[i].get_attribute("checked") != "true":
                check_boxes[i].click()
                count += 1
        if count >= 1:
            SeleniumCore.find_elements_by(*contributor_details.OVERRIDE_BUTTON)[0].click()

    def get_question_code_row_details(self, table_name, question):
        table = SeleniumCore.wait_for_element_to_be_displayed(By.ID, table_name)
        rows = table.find_elements_by_tag_name("tr")
        # Ignore the first row
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see if the question code matches
            if cols[0].text == question:
                return rows[i]

    def submit_question_value(self, survey, value_type, value, question):
        if value_type:
            self.submit_sales_value(survey, value, question)

    def submit_sales_value(self, survey, value, question):
        value = Utilities.convert_blank_data_value(value)
        question_element = Utilities.get_question_code_element(survey, question)
        SeleniumCore.set_current_data_text(question_element, value)

    def save_the_application(self):
        self.driver.find_element(
            *contributor_details.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.check_if_validation_status_changed()

    def refresh_the_form(self):
        self.driver.refresh()
        time.sleep(2)

    def get_validation_message(self, survey, exp_msg):
        if 'validation' in exp_msg:
            msg = ValidationMessages().get_expected_validation_message(survey, exp_msg)
        elif 'override message' in exp_msg:
            msg = OverrideMessages().get_expected_override_message(survey, exp_msg)
        else:
            msg = exp_msg
        return msg

    def get_no_of_validation_error_messages(self):
        return len(SeleniumCore.find_elements_by(By.XPATH, contributor_details.ERROR_MESSAGES_ELEMENT))

    def get_validation_status(self):
        return SeleniumCore.get_element_text(*contributor_details.STATUS)

    def validate_the_previous_period_details(self, *questions_and_values):
        self.submit_values_for_survey_questions(questions_and_values[0], questions_and_values[1],
                                                questions_and_values[2])
        self.save_the_application()
        SeleniumCore.close_the_current_window()

    def submit_values_for_survey_questions(self, *questions_and_values):
        global question_codes
        question_codes = questions_and_values
        survey = questions_and_values[0]
        questions_list = questions_and_values[1]
        commodity_values = Utilities.get_values_as_a_list(questions_and_values[2])

        if len(commodity_values) > 1 and type(questions_list) == list:
            self.submit_values_as_a_list_for_multiple_questions(survey, questions_list, commodity_values)
        elif len(commodity_values) == 1 and type(questions_list) == list:
            self.submit_single_value_for_multiple_questions(survey, questions_list, commodity_values[0])
        else:
            self.submit_single_value_per_question(survey, questions_list, commodity_values[0])

    def submit_values_as_a_list_for_multiple_questions(self, survey, questions_list, commodity_values):
        if len(questions_list) > 1:
            count = 0
        for question in questions_list:
            question_element = Utilities.get_question_code_element(survey, question)
            SeleniumCore.set_current_data_text(
                question_element, Utilities.convert_blank_data_value(commodity_values[count]))
            if len(commodity_values) > 1:
                count += 1

    def submit_single_value_for_multiple_questions(self, survey, questions_list, commodity_value):
        for question in questions_list:
            question_element = Utilities.get_question_code_element(survey, question)
            commodity_value = Utilities.convert_blank_data_value(commodity_value)
            SeleniumCore.set_current_data_text(question_element, commodity_value)

    def submit_single_value_per_question(self, survey, questions_list, commodity_value):
        question_element = Utilities.get_question_code_element(survey, questions_list)
        SeleniumCore.set_current_data_text(
            question_element, commodity_value)

    def validate_the_current_period_details(self, *questions_and_values):
        self.submit_values_for_survey_questions(questions_and_values[0], questions_and_values[1],
                                                questions_and_values[2])
        self.save_the_application()

    def run_the_validation_process(self, *questions):
        questions_list = questions[0]
        comparing_question_value = Utilities.convert_blank_data_value(questions[1])
        derived_question_value = Utilities.convert_blank_data_value(questions[2])
        survey = Utilities.convert_blank_data_value(questions[3])

        comparing_question_element = Utilities.get_question_code_element(survey, questions_list[0])
        derived_question_element = Utilities.get_question_code_element(survey, questions_list[1])
        SeleniumCore.set_current_data_text(comparing_question_element, comparing_question_value)
        ContributorDetailsPage().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(By.ID, derived_question_element)
        if derived_question_value == '':
            derived_question_value = '0'
        ReportingHelper.check_single_message_matches(questions_list[1], actual_derived_val, derived_question_value)
