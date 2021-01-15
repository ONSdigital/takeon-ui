from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.base_page import BasePage


class SubmitContributorDetails(BasePage):

    def __init__(self):
        if self.current_page_title() == 'Search':
            SeleniumCore.switch_window()
        super().__init__('Data Clearing')

    def submit_question_value(self, survey, value_type, value, question):
        if value_type:
            self.submit_sales_value(survey, value, question)

    def submit_sales_value(self, survey, value, question):
        value = Utilities.convert_blank_data_value(value)
        question_element = Utilities.get_question_code_element(survey, question)
        SeleniumCore.set_current_data_text(question_element, value)

    def submit_values_for_survey_questions(self, *questions_and_values):
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
