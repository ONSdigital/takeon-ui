from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.get_contributor_details import GetContributorDetails


class CheckMessagesContributorDetails:

    def check_validation_message(self, survey, question_type, exp_msg, is_validation_exists):
        self.check_if_overall_validation_triggered()
        exp_msg = GetContributorDetails().get_validation_message(survey, exp_msg)

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

    def check_validation_msg_matches(self, operator_type, comparison_val_one, comparison_val_two, result):
        self.check_if_overall_validation_triggered()
        ReportingHelper.compare_the_messages(operator_type, comparison_val_one, comparison_val_two, result)

    def check_multiple_comment_text_messages(self, question_codes):
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

    def check_if_overall_validation_triggered(self):
        if GetContributorDetails().get_no_of_validation_error_messages() >= 0:
            ReportingHelper.check_single_message_not_matches(
                GetContributorDetails().get_validation_status().lower(), 'form saved',
                '', 'Please check, Overall validation failed')

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
            comparison_val_two = self.check_for_zero_value(new_value_one, new_value_two,
                                                           threshold_value)
            self.check_validation_msg_matches(operator_type, comparison_val_one,
                                              comparison_val_two, result)

    def check_for_blank_validation(self, operator_type, value_one, value_two, result):
        value_one = Utilities.convert_blank_data_value(value_one)
        val_two = Utilities.convert_blank_data_value(value_two)
        self.check_validation_msg_matches(operator_type, value_one, val_two, result)

    def check_for_zero_value(self, value_one, value_two, threshold_value):
        if value_one == 0 and value_two == 0:
            comparison_val_two = value_two
        else:
            comparison_val_two = int(threshold_value)
        return comparison_val_two
