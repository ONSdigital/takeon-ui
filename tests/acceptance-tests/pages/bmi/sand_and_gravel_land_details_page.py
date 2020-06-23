from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.common.contributor_details_page import ContributorDetailsPage


class SandGravelLandAndMarineDetailsPage(ContributorDetailsPage):
    QUESTION_NO_146 = By.ID, '0146'
    QUESTION_NO_147 = By.ID, '0147'
    QUESTION_NO_148 = By.ID, '0148'
    question_codes = {
        '601': '0601',
        '602': '0602',
        '603': '0603',
    }

    question_codes_list = ["Q601", "Q602", "Q603", "Q604", "Q605", "Q606", "Q607", 'Q608']
    land_numeric_question_codes_list = ["Q146", "Q147"]
    marine_numeric_question_codes_list = ["Q146", "Q148"]
    QUESTION_146_ELEMENT = By.ID, '0146',
    QUESTION_147_ELEMENT = By.ID, '0147',
    QUESTION_148_ELEMENT = By.ID, '0148',
    COMMON_QUESTION_CODES_ELEMENTS = [(By.ID, '0601'), (By.ID, '0602'), (By.ID, '0603'), (By.ID, '0604'),
                                      (By.ID, '0605'),
                                      (By.ID, '0606'), (By.ID, '0607'), (By.ID, '0608'), (By.ID, '9001')]
    ERROR_MESSAGE_ELEMENT_STRING_PART_ONE = '//strong[contains(text(),"'
    ERROR_MESSAGE_ELEMENT_STRING_PART_TWO = '")]'

    def validate_the_previous_period_details(self, question_code, previous_value):
        self.submit_the_period_details(question_code, previous_value)
        self.driver.find_element(*SandGravelLandAndMarineDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        SeleniumCore.close_the_current_window()

    def validate_the_current_period_details(self, question_code, current_value):
        self.driver.refresh()
        self.submit_the_period_details(question_code, current_value)
        self.driver.find_element(*SandGravelLandAndMarineDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.driver.refresh()

    def submit_the_period_details(self, question_code, value):
        SeleniumCore.switch_window()
        question_code_ele = self.driver.find_element_by_id(self.question_codes.get(question_code))
        question_code_ele.clear()
        question_code_ele.send_keys(value)

    def check_threshold_value(self, previous_value, current_value):
        return int(current_value) - int(previous_value)

    def get_status(self):
        return SeleniumCore.get_element_text(*SandGravelLandAndMarineDetailsPage.STATUS)

    def get_validation_message(self):
        element_text = "This has changed significantly since the last submission"
        element = self.ERROR_MESSAGE_ELEMENT_STRING_PART_ONE + element_text + self.ERROR_MESSAGE_ELEMENT_STRING_PART_TWO
        return self.driver.find_element_by_xpath(element).text

    def submit_the_numeric_fields_values_for_survey(self, *questions):
        questions_list = questions[0]
        survey = questions[1]
        existing_value = questions[2]
        new_value = questions[3]
        SeleniumCore.switch_window()
        if survey == '0066':
            self.submit_the_numeric_fields_values(questions_list, existing_value)
            self.save_the_application()
            self.submit_the_numeric_fields_values(questions_list, new_value)
        elif survey == '0076':
            self.submit_the_numeric_fields_values(questions_list, existing_value)
            self.save_the_application()
            self.submit_the_numeric_fields_values(questions_list, new_value)

    def submit_the_numeric_fields_values(self, questions_list, value):
        for q in questions_list:
            if q == 'Q146':
                SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT, value)
            elif q == 'Q147':
                SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_147_ELEMENT, value)
            elif q == 'Q148':
                SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_148_ELEMENT, value)

    def submit_the_values_for_survey_question_codes(self, survey, existing_value, new_value):
        SeleniumCore.switch_window()
        if survey == '0066':
            self.submit_the_land_survey_values(existing_value)
            self.save_the_application()
            self.submit_the_land_survey_values(new_value)
        elif survey == '0076':
            self.submit_the_marine_survey_values(existing_value)
            self.save_the_application()
            self.submit_the_marine_survey_values(new_value)

    def submit_the_land_survey_values(self, value):
        SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT, value)
        SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_147_ELEMENT, value)
        self.submit_the_common_survey_values(value)

    def submit_the_marine_survey_values(self, value):
        SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT, value)
        SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_148_ELEMENT, value)
        self.submit_the_common_survey_values(value)

    def submit_the_common_survey_values(self, value):
        for question in self.COMMON_QUESTION_CODES_ELEMENTS:
            SeleniumCore.set_element_text(*question, value)

    def get_the_validation_messages_for_all_question_codes(self):
        error_msg_elements = self.driver.find_elements(
            self.NO_OF_VALIDATION_ELEMENTS)
        return error_msg_elements

    def get_the_fixed_validation_messages_for_all_question_codes(self):
        error_msg_elements = self.driver.find_elements(
            self.QUESTION_CODE_FIXED_VALIDATION_MESSAGES)
        return error_msg_elements

    def check_numeric_fields_fixed_validations_exists(self, survey, is_validation_exists):
        if survey == '0066':
            self.check_numeric_fixed_validation(self.land_numeric_question_codes_list, is_validation_exists)
        elif survey == '0076':
            self.check_numeric_fixed_validation(self.marine_numeric_question_codes_list, is_validation_exists)

    def check_fixed_validations_exists(self, survey, validation_message, is_validation_exists):
        count = 0
        # get the number of validation message groups exists for all questions
        elements = self.driver.find_elements(*SandGravelLandAndMarineDetailsPage.QUESTION_CODE_PANEL_CLASS_ELEMENTS)
        # iterate through the validation messages
        for i in range(1, len(elements) + 1):
            count += 1
            error_element = self.Q_CODE_PART_ONE + str(count) + self.Q_CODE_PART_TWO
            no_of_error_msgs_per_question = self.driver.find_elements_by_xpath(error_element)

            # check if any validation exists for a question
            self.check_fixed_validation_messages(survey, self.question_codes_list, is_validation_exists, i,
                                                 no_of_error_msgs_per_question, validation_message)
                            
    def submit_comment_value(self, comment, question):
        SeleniumCore.switch_window()
        if comment.lower() == 'empty' or comment.lower() == 'blank':
            comment = ''
        if question.upper() == 'Q146':
            SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_NO_146, comment)
        elif question.upper() == 'Q147':
            SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_NO_147, comment)
        elif question.upper() == 'Q148':
            SeleniumCore.set_element_text(*SandGravelLandAndMarineDetailsPage.QUESTION_NO_148, comment)
