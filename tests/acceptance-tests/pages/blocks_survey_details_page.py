from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.contributor_details_page import ContributorDetailsPage


class BlocksSurveyDetailsPage(ContributorDetailsPage):
    QUESTION_CODES = [
        (By.ID, '0101'), (By.ID, '0102'), (By.ID, '0103'), (By.ID, '0104'),
        (By.ID, '0111'), (By.ID, '0112'), (By.ID, '0113'), (By.ID, '0114'),
        (By.ID, '0121'), (By.ID, '0122'), (By.ID, '0123'), (By.ID, '0124'),
        (By.ID, '9001'), (By.ID, '9002'), (By.ID, '9003')]

    blocks_numeric_question_codes = {
        'Q145': '0145',
        'Q146': '0146'
    }

    question_codes_list = [
        'Q101', 'Q102', 'Q103', 'Q104', 'Q111', 'Q112', 'Q113', 'Q114', 'Q121', 'Q122', 'Q123', 'Q124',
        'Q9001', 'Q9002', 'Q9003']

    def submit_the_values_for_blocks_survey_question_codes(self, existing_value, new_value):
        SeleniumCore.switch_window()
        self.submit_the_blocks_question_values(existing_value)
        self.save_the_application()
        self.submit_the_blocks_question_values(new_value)

    def submit_the_blocks_question_values(self, value):
        for question in self.QUESTION_CODES:
            SeleniumCore.set_element_text(*question, value)

    def check_fixed_validations_exists(self, validation_message, is_validation_exists):
        count = 0
        # get the number of validation message groups exists for all questions
        elements = self.driver.find_elements(*BlocksSurveyDetailsPage.QUESTION_CODE_PANEL_CLASS_ELEMENTS)
        # iterate through the validation messages
        for i in range(1, len(elements) + 1):
            count += 1
            error_element = self.Q_CODE_PART_ONE + str(count) + self.Q_CODE_PART_TWO
            no_of_error_msgs_per_question = self.driver.find_elements_by_xpath(error_element)
            self.check_fixed_validation_messages('0073', self.question_codes_list, is_validation_exists, i,
                                                 no_of_error_msgs_per_question, validation_message)

    def submit_the_numeric_fields_values_for_survey(self, *questions):
        questions_list = questions[0]
        # survey = questions[1]
        existing_value = questions[2]
        new_value = questions[3]
        SeleniumCore.switch_window()
        self.submit_the_numeric_fields_values(questions_list, existing_value)
        self.save_the_application()
        self.submit_the_numeric_fields_values(questions_list, new_value)

    def submit_the_numeric_fields_values(self, questions_list, value):
        for question in questions_list:
            question_element = self.blocks_numeric_question_codes.get(question)
            self.driver.find_element_by_id(question_element).clear()
            self.driver.find_element_by_id(question_element).send_keys(value)

    def check_numeric_fields_fixed_validations_exists(self, is_validation_exists):
        self.check_numeric_fixed_validation(self.blocks_numeric_question_codes.keys(), is_validation_exists)
