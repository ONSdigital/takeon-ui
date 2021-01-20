from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from common.override_messages import OverrideMessages
from common.validation_messages import ValidationMessages
from pages.locators import contributor_details


class GetContributorDetails:

    def get_no_of_validation_error_messages_per_question(self, question):
        self.override_the_validation(question, 'validation')
        question_row = self.get_question_code_row_details(contributor_details.CURRENT_DATA_TAB_ELEMENT, question)
        elements = contributor_details.ERROR_MESSAGES_COLUMN + contributor_details.ERROR_MESSAGES_ELEMENT
        return question_row.find_elements(By.XPATH, elements)

    def get_question_code_row_details(self, table_name, question):
        table = SeleniumCore.wait_for_element_to_be_displayed(By.ID, table_name)
        rows = table.find_elements_by_tag_name("tr")
        # Ignore the first row
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see if the question code matches
            if cols[0].text == question:
                return rows[i]

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

    def override_the_validation(self, question, type_of_check):
        question_row = self.get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question)
        check_boxes = question_row.find_elements_by_name(contributor_details.OVERRIDE_CHECKBOX_ELEMENT)
        count = 0
        for i in range(0, len(check_boxes)):
            if type_of_check == 'validation' and check_boxes[i].get_attribute("checked") == "true" or \
                    type_of_check == 'override' and check_boxes[i].get_attribute("checked") != "true":
                check_boxes[i].click()
                count += 1
        if count >= 1:
            SeleniumCore.find_elements_by(*contributor_details.OVERRIDE_BUTTON)[0].click()
