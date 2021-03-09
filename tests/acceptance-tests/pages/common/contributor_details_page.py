from base.selenium_core import SeleniumCore
from pages.common.base_page import BasePage
from pages.common.contributor_details.check_values_contributor_details import CheckValuesContributorDetails
from pages.common.contributor_details.check_messages_contributor_details import CheckMessagesContributorDetails
from pages.common.contributor_details.contributor_override_details import ContributorOverrideDetails
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.common.contributor_details.submit_contributor_details import SubmitContributorDetails
from pages.common.contributor_details.validate_contributor_details import ValidateContributorDetails


class ContributorDetailsPage(BasePage):

    def __init__(self):
        if self.current_page_title() == 'Search':
            SeleniumCore.switch_window()
        super().__init__('Data Clearing')

    # SubmitContributorDetails

    def submit_question_value(self, period,period_start_date, survey, value_type, value, question):
        SubmitContributorDetails().submit_question_value(period,period_start_date, survey, value_type, value, question)

    def submit_values_for_survey_questions(self, *questions_and_values):
        SubmitContributorDetails().submit_values_for_survey_questions(questions_and_values)

    # GetContributorDetails

    def override_the_validation(self, question, type_of_check):
        GetContributorDetails().override_the_validation(question, type_of_check)

    # ValidateContributorDetails

    def run_the_validation_process(self, *questions):
        ValidateContributorDetails().run_the_validation_process(questions)

    def validate_the_previous_period_details(self, *questions_and_values):
        ValidateContributorDetails().validate_the_previous_period_details(questions_and_values)

    def validate_the_current_period_details(self, *questions_and_values):
        ValidateContributorDetails().validate_the_current_period_details(questions_and_values)

    # CheckContributorDetails

    def save_the_application(self):
        CheckValuesContributorDetails().save_the_application()

    def check_multiple_comment_text_messages(self, *question_codes):
        CheckMessagesContributorDetails().check_multiple_comment_text_messages(question_codes)

    def check_validation_message(self, survey, question_type, exp_msg, is_validation_exists):
        CheckMessagesContributorDetails().check_validation_message(survey, question_type, exp_msg, is_validation_exists)

    def check_multiple_questions_validation_messages(self, survey, question_codes, exp_msg, is_validation_exists):
        CheckMessagesContributorDetails().check_multiple_questions_validation_messages(survey, question_codes, exp_msg,
                                                                                       is_validation_exists)

    def check_turnover_ratio(self, operator_type, internet_sales, total_sales, threshold_value, result):
        CheckMessagesContributorDetails().check_turnover_ratio(operator_type, internet_sales, total_sales,
                                                               threshold_value,
                                                               result)

    def check_absolute_difference_validation(self, operator_type, value_one, value_two, threshold_value, result):
        CheckMessagesContributorDetails().check_absolute_difference_validation(operator_type, value_one, value_two,
                                                                               threshold_value, result)

    def check_values_are_not_equal(self, question, comparison_val_one, comparison_val_two, result):
        CheckValuesContributorDetails().check_values_are_not_equal(question, comparison_val_one, comparison_val_two,
                                                                   result)

    def check_values_movement_to_or_from_zero(self, question_codes, comparison_val_one, comparison_val_two, result):
        CheckValuesContributorDetails().check_values_movement_to_or_from_zero(question_codes, comparison_val_one,
                                                                              comparison_val_two, result)

    def check_the_override_message(self, survey, question_code, exp_msg):
        ContributorOverrideDetails().check_the_override_message(survey, question_code, exp_msg)

    def check_the_override_checkbox_displayed(self, question):
        ContributorOverrideDetails().check_the_override_checkbox_displayed(question)
