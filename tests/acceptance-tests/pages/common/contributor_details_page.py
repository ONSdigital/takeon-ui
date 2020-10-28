import time
from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from common.override_messages import OverrideMessages
from common.validation_messages import ValidationMessages
from pages.common.base_page import BasePage


class ContributorDetailsPage(BasePage):

    def __init__(self):
        if self.current_page_title() == 'Search':
            SeleniumCore.switch_window()
        super().__init__('Data Clearing')

    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    STATUS = By.XPATH, '//span[contains(@title,"Status")]'
    ERROR_MESSAGES_ELEMENT = '//p[@class="panel__error u-mb-no"]'
    OVERRIDE_MESSAGE_LABEL = '//label'
    CURRENT_PERIOD_COLUMN = 'td[2]'
    ERROR_MESSAGES_COLUMN = 'td[4]'
    OVERRIDE_BUTTON = By.ID, 'override_button'
    OVERRIDE_MESSAGE_ELEMENT = By.CLASS_NAME, 'checkbox__label to-u-bg'
    CURRENT_DATA_TAB_ELEMENT = 'tabId1'
    HISTORIC_DATA_TAB_ELEMENT = 'tabId2'
    OVERRIDE_CHECKBOX_ELEMENT = 'override-checkbox'

    def get_no_of_validation_error_messages_per_question(self, question):
        self.override_the_validation(question, 'validation')
        question_row = self.get_question_code_row_details(self.CURRENT_DATA_TAB_ELEMENT, question)
        elements = self.ERROR_MESSAGES_COLUMN + self.ERROR_MESSAGES_ELEMENT
        return question_row.find_elements(By.XPATH, elements)

    def override_the_validation(self, question, type_of_check):
        question_row = self.get_question_code_row_details(self.CURRENT_DATA_TAB_ELEMENT, question)
        check_boxes = question_row.find_elements_by_name(self.OVERRIDE_CHECKBOX_ELEMENT)
        count = 0
        for i in range(0, len(check_boxes)):
            if type_of_check == 'validation' and check_boxes[i].get_attribute("checked") == "true" or \
                    type_of_check == 'override' and check_boxes[i].get_attribute("checked") != "true":
                check_boxes[i].click()
                count += 1
        if count >= 1:
            SeleniumCore.find_elements_by(*ContributorDetailsPage.OVERRIDE_BUTTON)[0].click()

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
            *ContributorDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.check_if_validation_status_changed()

    def check_if_validation_status_changed(self):
        i = 0
        while i < 3:
            status = self.get_validation_status().lower()

            if status == 'check needed':
                if i > 0:
                    break
                self.refresh_the_form()
            elif status != 'check needed':
                self.refresh_the_form()
            i += 1

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

    def check_validation_message(self, survey, question_type, exp_msg, is_validation_exists):
        self.check_if_overall_validation_triggered()
        exp_msg = self.get_validation_message(survey, exp_msg)
        if type(question_type) == list and len(question_type) > 1:
            self.check_multiple_comment_text_messages(survey)
        else:
            no_of_msgs = ContributorDetailsPage().get_no_of_validation_error_messages_per_question(question_type)
            if len(no_of_msgs) == 0:
                if is_validation_exists == 'be':
                    ReportingHelper.check_elements_message_matches(
                        question_type, no_of_msgs, exp_msg)
                elif is_validation_exists == 'not be':
                    act_msg = ''
                    ReportingHelper.check_multiple_messages_not_matches(
                        question_type, act_msg, exp_msg)
            elif len(no_of_msgs) > 0:
                if is_validation_exists == 'be':
                    ReportingHelper.check_elements_message_matches(
                        question_type, no_of_msgs, exp_msg)
                elif is_validation_exists == 'not be':
                    ReportingHelper.check_multiple_messages_not_matches(
                        question_type, no_of_msgs, exp_msg)

    def check_multiple_questions_validation_messages(self, survey, question_codes, exp_msg, is_validation_exists):
        self.check_if_overall_validation_triggered()
        if len(question_codes) > 1:
            for question in question_codes:
                self.check_validation_message(survey, question, exp_msg, is_validation_exists)

    def check_turnover_ratio(self, operator_type, internet_sales, total_sales, threshold_value, result):
        comparison_val_one = int(internet_sales)
        thre_val = float(threshold_value[:-1]) / 100
        comparison_val_two = thre_val * int(total_sales)
        self.check_validation_msg_matches(
            operator_type, comparison_val_one, comparison_val_two, result)

    def check_absolute_difference_validation(self, operator_type, value_one, value_two, threshold_value,
                                             result):
        if value_one == 'blank' and value_two == 'blank':
            self.check_for_blank_validation(operator_type, value_one, value_two, result)
        else:
            new_value_one = int(value_one)
            new_value_two = int(value_two)
            comparison_val_one = abs(new_value_one - new_value_two)
            comparison_val_two = self.check_for_zero_value(new_value_one, new_value_two, threshold_value)
            self.check_validation_msg_matches(operator_type, comparison_val_one, comparison_val_two, result)

    def check_for_zero_value(self, value_one, value_two, threshold_value):
        if value_one == 0 and value_two == 0:
            comparison_val_two = value_two
        else:
            comparison_val_two = int(threshold_value)
        return comparison_val_two

    def check_for_blank_validation(self, operator_type, value_one, value_two, result):
        value_one = Utilities.convert_blank_data_value(value_one)
        val_two = Utilities.convert_blank_data_value(value_two)
        self.check_validation_msg_matches(operator_type, value_one, val_two, result)

    def check_validation_msg_matches(self, operator_type, comparison_val_one, comparison_val_two, result):
        self.check_if_overall_validation_triggered()
        ReportingHelper.compare_the_messages(operator_type, comparison_val_one, comparison_val_two, result)

    def check_values_are_not_equal(self, question, comparison_val_one, comparison_val_two, result):
        self.check_if_overall_validation_triggered()
        if comparison_val_one == 'blank' and comparison_val_two == 'blank':
            comparison_val_one = Utilities.convert_blank_data_value(comparison_val_one)
            comparison_val_two = Utilities.convert_blank_data_value(comparison_val_two)
            is_validation_exists = ReportingHelper.compare_strings(comparison_val_one,
                                                                   comparison_val_two)

        else:
            is_validation_exists = ReportingHelper.compare_values_are_not_equal(comparison_val_one,
                                                                                comparison_val_two)
        ReportingHelper.check_single_message_matches(
            question, result, str(is_validation_exists).lower())

    def check_values_movement_to_or_from_zero(self, question_codes, comparison_val_one, comparison_val_two, result):
        self.check_if_overall_validation_triggered()
        if len(question_codes) > 1:
            for question in question_codes:
                if comparison_val_one == 'blank' and comparison_val_two == 'blank':
                    value_one = Utilities.convert_blank_data_value(comparison_val_one)
                    value_two = Utilities.convert_blank_data_value(comparison_val_two)
                    is_validation_exists = ReportingHelper.compare_strings(value_one,
                                                                           value_two)

                else:
                    is_validation_exists = ReportingHelper.compare_the_zero_movement_values(comparison_val_one,
                                                                                            comparison_val_two)
                ReportingHelper.check_single_message_matches(
                    question, result, str(is_validation_exists).lower())

    def get_no_of_validation_error_messages(self):
        return len(SeleniumCore.find_elements_by(By.XPATH, self.ERROR_MESSAGES_ELEMENT))

    def get_validation_status(self):
        return SeleniumCore.get_element_text(*ContributorDetailsPage.STATUS)

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

    def check_if_overall_validation_triggered(self):
        if self.get_no_of_validation_error_messages() >= 0:
            ReportingHelper.check_single_message_not_matches(
                self.get_validation_status().lower(), 'form saved',
                '', 'Please check, Overall validation failed')

    def check_multiple_comment_text_messages(self, survey):
        global question_codes
        questions_list = question_codes[1]
        commodity_values = Utilities.get_values_as_a_list(question_codes[2])
        if len(questions_list) > 1:
            count = 0
            for question in questions_list:
                question_element = Utilities.get_question_code_element(survey, question)
                question_actual_text = SeleniumCore.get_attribute_element_text(By.ID, question_element)
                commodity_value = Utilities.convert_blank_data_value(commodity_values[count])
                ReportingHelper.check_single_message_matches(question_element, question_actual_text,
                                                             commodity_value)

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

    def check_the_override_message(self, survey, question_code, exp_msg):
        exp_msg = self.get_validation_message(survey, exp_msg)
        question_row = self.get_question_code_row_details(self.CURRENT_DATA_TAB_ELEMENT, question_code)
        elements = self.ERROR_MESSAGES_COLUMN + self.OVERRIDE_MESSAGE_LABEL
        override_messages_elements = question_row.find_elements(By.XPATH, elements)
        ReportingHelper.check_elements_message_matches(question_code, override_messages_elements, exp_msg)

    def check_the_override_checkbox_displayed(self, question):
        question_row = self.get_question_code_row_details(self.CURRENT_DATA_TAB_ELEMENT, question)
        check_boxes = question_row.find_elements(By.NAME, self.OVERRIDE_CHECKBOX_ELEMENT)
        ReportingHelper.compare_values(len(check_boxes), 1)
