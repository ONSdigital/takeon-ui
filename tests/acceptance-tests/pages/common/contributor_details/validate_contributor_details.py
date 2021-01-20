from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.check_values_contributor_details import CheckValuesContributorDetails
from pages.common.contributor_details.submit_contributor_details import SubmitContributorDetails


class ValidateContributorDetails:

    def run_the_validation_process(self, questions):
        questions_list = questions[0]
        comparing_question_value = Utilities.convert_blank_data_value(questions[1])
        derived_question_value = Utilities.convert_blank_data_value(questions[2])
        survey = Utilities.convert_blank_data_value(questions[3])

        comparing_question_element = Utilities.get_question_code_element(survey, questions_list[0])
        derived_question_element = Utilities.get_question_code_element(survey, questions_list[1])
        SeleniumCore.set_current_data_text(comparing_question_element, comparing_question_value)
        CheckValuesContributorDetails().save_the_application()
        actual_derived_val = SeleniumCore.get_attribute_element_text(By.ID, derived_question_element)
        if derived_question_value == '':
            derived_question_value = '0'
        ReportingHelper.check_single_message_matches(questions_list[1], actual_derived_val, derived_question_value)

    def validate_the_previous_period_details(self, questions_and_values):
        SubmitContributorDetails().submit_values_for_survey_questions(questions_and_values[0], questions_and_values[1],
                                                                      questions_and_values[2])
        CheckValuesContributorDetails().save_the_application()
        SeleniumCore.close_the_current_window()

    def validate_the_current_period_details(self, questions_and_values):
        SubmitContributorDetails().submit_values_for_survey_questions(questions_and_values[0], questions_and_values[1],
                                                                      questions_and_values[2])
        CheckValuesContributorDetails().save_the_application()
