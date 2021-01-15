import time

from selenium.webdriver.common.by import By

from base.driver_context import DriverContext
from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.common.contributor_details.submit_contributor_details import SubmitContributorDetails
from pages.locators import contributor_details


class CheckContributorDetails:

    def check_if_validation_status_changed(self):
        i = 0
        while i < 3:
            status = GetContributorDetails().get_validation_status().lower()

            if status == 'check needed':
                if i > 0:
                    break
                self.refresh_the_form()
            elif status != 'check needed':
                self.refresh_the_form()
            i += 1

    def refresh_the_form(self):
        DriverContext.driver.refresh()
        time.sleep(2)

    def save_the_application(self):
        DriverContext.driver.find_element(
            *contributor_details.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.check_if_validation_status_changed()

    def check_validation_message(self, survey, question_type, exp_msg, is_validation_exists):
        self.check_if_overall_validation_triggered()
        exp_msg = GetContributorDetails().get_validation_message(survey, exp_msg)
        #
        # if type(question_type) == list and len(question_type) > 1:
        #     self.check_multiple_comment_text_messages(survey, question_type, values)
        # else:
        no_of_msgs = GetContributorDetails().get_no_of_validation_error_messages_per_question(
            question_type)
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
        if type(question_codes) == list and len(question_codes) > 1:
            for question in question_codes:
                self.check_validation_message(survey, question, exp_msg, is_validation_exists)
        else:
            self.check_validation_message(survey, question_codes, exp_msg, is_validation_exists)

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

    def check_if_overall_validation_triggered(self):
        if GetContributorDetails().get_no_of_validation_error_messages() >= 0:
            ReportingHelper.check_single_message_not_matches(
                GetContributorDetails().get_validation_status().lower(), 'form saved',
                '', 'Please check, Overall validation failed')

    def check_multiple_comment_text_messages(self, *question_codes):
        survey = question_codes[0]
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

    def check_the_override_message(self, survey, question_code, exp_msg):
        exp_msg = GetContributorDetails().get_validation_message(survey, exp_msg)
        question_row = GetContributorDetails().get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question_code)
        elements = contributor_details.ERROR_MESSAGES_COLUMN + contributor_details.OVERRIDE_MESSAGE_LABEL
        override_messages_elements = question_row.find_elements(By.XPATH, elements)
        ReportingHelper.check_elements_message_matches(question_code, override_messages_elements, exp_msg)

    def check_the_override_checkbox_displayed(self, question):
        question_row = GetContributorDetails().get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question)
        check_boxes = question_row.find_elements(By.NAME, contributor_details.OVERRIDE_CHECKBOX_ELEMENT)
        ReportingHelper.compare_values(len(check_boxes), 1)
