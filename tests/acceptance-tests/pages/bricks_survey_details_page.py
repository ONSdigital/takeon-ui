from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.contributor_details_page import ContributorDetailsPage


class BricksSurveyDetailsPage(ContributorDetailsPage):
    QUESTION_CODES = [
        (By.ID, '0001'), (By.ID, '0002'), (By.ID, '0003'), (By.ID, '0004'),
        (By.ID, '0011'), (By.ID, '0012'), (By.ID, '0013'), (By.ID, '0014'),
        (By.ID, '0021'), (By.ID, '0022'), (By.ID, '0023'), (By.ID, '0024'),
        (By.ID, '0145'), (By.ID, '0146'), (By.ID, '0501'), (By.ID, '0502'),
        (By.ID, '0503'), (By.ID, '0504'), (By.ID, '8000'), (By.ID, '9204'),
        (By.ID, '9214'), (By.ID, '9224'), (By.ID, '9501'), (By.ID, '9502'),
        (By.ID, '9503'), (By.ID, '9504')]

    bricks_numeric_question_codes = {
        'Q145': '0145',
        'Q146': '0146',
        'Q8000': '8000'
    }

    question_codes_list = [
        'Q001', 'Q002', 'Q003', 'Q004', 'Q011', 'Q012', 'Q013', 'Q014', 'Q021', 'Q022', 'Q023', 'Q024',
        'Q501', 'Q502', 'Q503', 'Q504', 'Q8000', 'Q9204', 'Q9214', 'Q9224', 'Q9501', 'Q9502', 'Q9503', 'Q9504']

    def submit_the_values_for_bricks_survey_question_codes(self, existing_value, new_value):
        SeleniumCore.switch_window()
        self.submit_the_bricks_question_values(existing_value)
        self.save_the_application()
        self.submit_the_bricks_question_values(new_value)

    def submit_the_bricks_question_values(self, value):
        for question in self.QUESTION_CODES:
            SeleniumCore.set_element_text(*question, value)

    def check_fixed_validations_exists(self, survey, validation_message, is_validation_exists):
        count = 0
        # get the number of validation message groups exists for all questions
        elements = self.driver.find_elements(*ContributorDetailsPage.QUESTION_CODE_PANEL_CLASS_ELEMENTS)
        # iterate through the validation messages
        for i in range(1, len(elements) + 1):
            count += 1
            error_element = self.Q_CODE_PART_ONE + str(count) + self.Q_CODE_PART_TWO
            no_of_error_msgs_per_question = self.driver.find_elements_by_xpath(error_element)

            # check if any validation exists for a question
            self.check_fixed_validation_messages(survey, self.question_codes_list, is_validation_exists, i,
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
            question_element = self.bricks_numeric_question_codes.get(question)
            self.driver.find_element_by_id(question_element).clear()
            self.driver.find_element_by_id(question_element).send_keys(value)

    def check_numeric_fields_fixed_validations_exists(self, is_validation_exists):
        self.check_numeric_fixed_validation(self.bricks_numeric_question_codes.keys(), is_validation_exists)
