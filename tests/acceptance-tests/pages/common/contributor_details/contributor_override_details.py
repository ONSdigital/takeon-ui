from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.locators import contributor_details


class ContributorOverrideDetails:

    def check_the_override_message(self, survey, question_code, exp_msg):
        exp_msg = GetContributorDetails().get_validation_message(survey, exp_msg)
        question_row = GetContributorDetails().get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question_code)
        elements = contributor_details.ERROR_MESSAGES_COLUMN + contributor_details.ERROR_LABEL
        override_messages_elements = question_row.find_elements(By.XPATH, elements)
        ReportingHelper.check_elements_message_matches(question_code, override_messages_elements, exp_msg)

    def check_the_override_checkbox_displayed(self, question):
        question_row = GetContributorDetails().get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question)
        check_boxes = question_row.find_elements(By.NAME, contributor_details.OVERRIDE_CHECKBOX_ELEMENT)
        ReportingHelper.compare_values(len(check_boxes), 1)
