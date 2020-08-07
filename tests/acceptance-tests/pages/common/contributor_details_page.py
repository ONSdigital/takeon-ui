import time
from selenium.webdriver.common.by import By
from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.base_page import BasePage
import numpy as np


class ContributorDetailsPage(BasePage):
    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    STATUS = By.XPATH, '//span[contains(@title,"Status")]'
    QUESTION_PANEL_ERROR_MESSAGE_ELEMENT_ONE = '//*[@id="responseForm"]/div/div/p/label[contains(text(),"'
    QUESTION_PANEL_ERROR_MESSAGE_ELEMENT_TWO = '")]/../../p[@class="panel__error u-mb-no"]'
    ERROR_MESSAGES_ELEMENT = By.XPATH, '//p[@class="panel__error u-mb-no"]'

    def get_validation_error_message(self, question_type):
        element = self.QUESTION_PANEL_ERROR_MESSAGE_ELEMENT_ONE + \
                  question_type + self.QUESTION_PANEL_ERROR_MESSAGE_ELEMENT_TWO
        return SeleniumCore.find_elements_by_xpath(element)

    def submit_question_value(self, value_type, value, question):
        SeleniumCore.switch_window()
        if value_type:
            self.submit_sales_value(value, question)

    def submit_sales_value(self, value, question):
        value = Utilities.convert_blank_data_value(value)
        SeleniumCore.set_element_text_by_id(Utilities.get_question_code_element(question), value)

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

    def check_validation_message(self, question_type, exp_msg, is_validation_exists):
        self.check_if_overall_validation_triggered()
        if type(question_type) == list and len(question_type) > 1:
            self.check_multiple_comment_text_messages()
        else:
            no_of_msgs = ContributorDetailsPage().get_validation_error_message(question_type)
            if len(no_of_msgs) == 1:
                actual_msg = no_of_msgs[0].text
                if is_validation_exists == 'be':
                    ReportingHelper.check_single_message_matches(
                        question_type, actual_msg, exp_msg)
                elif is_validation_exists == 'not be':
                    ReportingHelper.check_single_message_not_matches(
                        actual_msg, exp_msg, question_type)
            elif len(no_of_msgs) == 2:
                if is_validation_exists == 'be':
                    ReportingHelper.check_multiple_messages_matches(
                        question_type, no_of_msgs, exp_msg)
                elif is_validation_exists == 'not be':
                    ReportingHelper.check_multiple_messages_not_matches(
                        question_type, no_of_msgs, exp_msg)
            elif len(no_of_msgs) == 0:
                act_msg = ''
                ReportingHelper.check_multiple_messages_not_matches(
                    question_type, act_msg, exp_msg)

    def check_multiple_questions_validation_messages(self, question_codes, exp_msg, is_validation_exists):
        self.check_if_overall_validation_triggered()
        if len(question_codes) > 1:
            for question in question_codes:
                self.check_validation_message(
                    question, exp_msg, is_validation_exists)

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
            is_validation_exists = ReportingHelper.compare_values(comparison_val_one,
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
        return len(SeleniumCore.find_elements_by(*ContributorDetailsPage.ERROR_MESSAGES_ELEMENT))

    def get_validation_status(self):
        return SeleniumCore.get_element_text(*ContributorDetailsPage.STATUS)

    def validate_the_previous_period_details(self, *questions_and_values):
        self.submit_values_for_survey_questions(questions_and_values[0], questions_and_values[1])
        self.save_the_application()
        SeleniumCore.close_the_current_window()

    def submit_values_for_survey_questions(self, *questions_and_values):
        global question_codes
        question_codes = questions_and_values
        SeleniumCore.switch_window()
        questions_list = questions_and_values[0]
        new_questions_list = np.asarray(questions_list)
        commodity_values = Utilities.get_values_as_a_list(questions_and_values[1])

        if len(commodity_values) > 1 and new_questions_list.size > 1:
            self.submit_values_as_a_list_for_multiple_questions(questions_list, commodity_values)
        elif new_questions_list.size > 1 and len(commodity_values) == 1:
            self.submit_single_value_for_multiple_questions(questions_list, commodity_values[0])
        else:
            self.submit_single_value_per_question(questions_list, commodity_values[0])

    def submit_values_as_a_list_for_multiple_questions(self, questions_list, commodity_values):
        new_questions_list = np.asarray(questions_list)
        if new_questions_list.size > 1:
            count = 0
        for question in questions_list:
            question_element = Utilities.get_question_code_element(question)
            SeleniumCore.set_element_text_by_id(
                question_element, Utilities.convert_blank_data_value(commodity_values[count]))
            if len(commodity_values) > 1:
                count += 1

    def submit_single_value_for_multiple_questions(self, questions_list, commodity_value):
        for question in questions_list:
            question_element = Utilities.get_question_code_element(question)
            commodity_value = Utilities.convert_blank_data_value(commodity_value)
            SeleniumCore.set_element_text_by_id(question_element, commodity_value)

    def submit_single_value_per_question(self, questions_list, commodity_value):
        question_element = Utilities.get_question_code_element(questions_list)
        SeleniumCore.set_element_text_by_id(
            question_element, commodity_value)

    def validate_the_current_period_details(self, *questions_and_values):
        self.submit_values_for_survey_questions(questions_and_values[0], questions_and_values[1])
        self.save_the_application()

    def check_if_overall_validation_triggered(self):
        if self.get_no_of_validation_error_messages() >= 0:
            ReportingHelper.check_single_message_not_matches(
                self.get_validation_status().lower(), 'form saved',
                '', 'Please check, Overall validation failed')

    def check_multiple_comment_text_messages(self):
        global question_codes
        questions_list = question_codes[0]
        commodity_values = Utilities.get_values_as_a_list(question_codes[1])
        new_questions_list = np.asarray(questions_list)
        if new_questions_list.size > 1:
            count = 0
            for question in questions_list:
                question_element = Utilities.get_question_code_element(question)
                question_actual_text = SeleniumCore.get_attribute_element_text(By.ID, question_element)
                commodity_value = Utilities.convert_blank_data_value(commodity_values[count])
                ReportingHelper.check_single_message_matches(question_element, question_actual_text,
                                                             commodity_value)

    def run_the_validation_process(self, *questions):
        questions_list = questions[0]
        comparing_question_value = Utilities.convert_blank_data_value(questions[1])
        derived_question_value = Utilities.convert_blank_data_value(questions[2])
        comparing_question_element = Utilities.get_question_code_element(questions_list[0])
        derived_question_element = Utilities.get_question_code_element(questions_list[1])
        SeleniumCore.set_element_text_by_id(comparing_question_element, comparing_question_value)
        ContributorDetailsPage().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(By.ID, derived_question_element)
        if derived_question_value == '':
            derived_question_value = '0'
        ReportingHelper.check_single_message_matches(questions_list[1], actual_derived_val, derived_question_value)
