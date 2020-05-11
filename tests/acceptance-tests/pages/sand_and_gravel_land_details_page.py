from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage


class SandGravelLandAndMarineDetailsPage(BasePage):
    question_codes = {
        '601': '0601',
        '602': '0602',
        '603': '0603',
    }

    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    STATUS = By.XPATH, "//span[@class='status status--error']"
    QUESTION_PANEL_ERROR_MESSAGE = By.XPATH, "//div[1]/div[1]/p[1]/strong[1]"
    QUESTION_CODE_FIXED_VALIDATION_MESSAGES = By.XPATH, '//*[@id="responseForm"]/div/div/p[2]/strong'
    QUESTION_CODE_PANELS_ERROR_MESSAGES = By.XPATH, '//*[@id="responseForm"]/div/div/p/strong'
    QUESTION_CODE_PANEL_CLASS_ELEMENTS = By.XPATH, "//div[@class='panel panel--error panel--simple']"
    Q_CODE_VALIDATION_ONE = '//div[@class="panel panel--error panel--simple"]//label[contains(text(),"'
    Q_CODE_PART_ONE = '//*[@id="responseForm"]/div['
    Q_CODE_PART_TWO = ']/div/p/strong'
    Q_CODE_PART_THREE = '")]'

    question_codes_list = ["Q601", "Q602", "Q603", "Q604", "Q605", "Q606", "Q607", 'Q608']
    land_numeric_question_codes_list = ["Q146", "Q147"]
    marine_numeric_question_codes_list = ["Q146", "Q148"]
    QUESTION_146_ELEMENT = By.ID, '0146',
    QUESTION_147_ELEMENT = By.ID, '0147',
    QUESTION_148_ELEMENT = By.ID, '0148',
    COMMON_QUESTION_CODES_ELEMENTS = [(By.ID, '0601'), (By.ID, '0602'), (By.ID, '0603'), (By.ID, '0604'),
                                      (By.ID, '0605'),
                                      (By.ID, '0606'), (By.ID, '0607'), (By.ID, '0608'), (By.ID, '9001')]

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
        question_code_ele = self.driver.find_element_by_id(self.get_question_codes(question_code))
        question_code_ele.clear()
        question_code_ele.send_keys(value)

    def get_question_codes(self, question_code):
        return self.question_codes[question_code]

    def check_threshold_value(self, previous_value, current_value):
        return int(current_value) - int(previous_value)

    def get_status(self, status_type):
        return self.driver.find_element(*SandGravelLandAndMarineDetailsPage.STATUS).text

    def get_validation_message(self):
        return self.driver.find_element(*SandGravelLandAndMarineDetailsPage.QUESTION_PANEL_ERROR_MESSAGE).text

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
                SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT).send_keys(value)
            elif q == 'Q147':
                SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_147_ELEMENT).send_keys(value)
            elif q == 'Q148':
                SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_148_ELEMENT).send_keys(value)

    def submit_the_values_for_land_survey_question_codes(self, existing_value, new_value):
        SeleniumCore.switch_window()
        self.submit_the_land_survey_values(existing_value)
        self.save_the_application()
        self.submit_the_land_survey_values(new_value)

    def submit_the_values_for_marine_survey_question_codes(self, existing_value, new_value):
        SeleniumCore.switch_window()
        self.submit_the_marine_survey_values(existing_value)
        self.save_the_application()
        self.submit_the_marine_survey_values(new_value)

    def save_the_application(self):
        self.driver.find_element(*SandGravelLandAndMarineDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.driver.refresh()

    def submit_the_land_survey_values(self, value):
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_147_ELEMENT).send_keys(value)
        self.submit_the_common_survey_values(value)

    def submit_the_marine_survey_values(self, value):
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_148_ELEMENT).send_keys(value)
        self.submit_the_common_survey_values(value)

    def submit_the_common_survey_values(self, value):
        for question in self.COMMON_QUESTION_CODES_ELEMENTS:
            SeleniumCore.find_element_by(*question).send_keys(value)

    def get_the_validation_messages_for_all_question_codes(self):
        error_msg_elements = self.driver.find_elements(
            *SandGravelLandAndMarineDetailsPage.QUESTION_CODE_PANELS_ERROR_MESSAGES)
        return error_msg_elements

    def get_the_fixed_validation_messages_for_all_question_codes(self):
        error_msg_elements = self.driver.find_elements(
            *SandGravelLandAndMarineDetailsPage.QUESTION_CODE_FIXED_VALIDATION_MESSAGES)
        return error_msg_elements

    def check_numeric_fields_fixed_validations_exists(self, survey, is_validation_exists):

        if survey == '0066':
            self.check_numeric_fixed_validation(self.land_numeric_question_codes_list, is_validation_exists)
        elif survey == '0076':
            self.check_numeric_fixed_validation(self.marine_numeric_question_codes_list, is_validation_exists)

    def check_numeric_fixed_validation(self, questions_list, is_validation_exists):
        # iterate through the list of expected question codes
        for i in range(0, len(questions_list)):
            question_validation_ele = self.Q_CODE_VALIDATION_ONE + questions_list[
                i] + self.Q_CODE_PART_THREE
            # check if any validation exists for a question
            if len(self.driver.find_elements_by_xpath(question_validation_ele)) > 0:
                assert False
            else:
                assert is_validation_exists == 'not'

    def check_fixed_validations_exists(self, validation_message, is_validation_exists):
        count = 0
        # get the number of validation message groups exists for all questions
        elements = self.driver.find_elements(*SandGravelLandAndMarineDetailsPage.QUESTION_CODE_PANEL_CLASS_ELEMENTS)
        # iterate through the validation messages
        for i in range(1, len(elements) + 1):
            count += 1
            error_element = self.Q_CODE_PART_ONE + str(count) + self.Q_CODE_PART_TWO
            no_of_error_msgs_per_question = self.driver.find_elements_by_xpath(error_element)

            # check if any validation exists for a question
            self.check_fixed_validation_msgs(is_validation_exists, i, no_of_error_msgs_per_question,
                                             validation_message)

    def check_fixed_validation_msgs(self, is_validation_exists, i, no_of_error_msgs, actual_msg):
        if is_validation_exists == 'be':
            if len(no_of_error_msgs) == 1:
                self.check_fixed_val_msgs(actual_msg, no_of_error_msgs[0].text, i)
            elif len(no_of_error_msgs) == 2:
                self.check_fixed_val_msgs(actual_msg, no_of_error_msgs[1].text, i)
            elif len(no_of_error_msgs) == 0:
                print("No validation exists for the question code: " + self.question_codes_list[i - 1])

        elif is_validation_exists == 'not be':
            if len(no_of_error_msgs) == 1:
                self.check_no_fixed_val_msgs(actual_msg, no_of_error_msgs[0].text, i)
            elif len(no_of_error_msgs) == 2:
                self.check_no_fixed_val_msgs(actual_msg, no_of_error_msgs[1].text, i)
            elif len(no_of_error_msgs) == 0:
                print("No validation exists for the question code: " + self.question_codes_list[i - 1])

    def check_fixed_val_msgs(self, actual_msg, exp_msg, i):
        if actual_msg == exp_msg:
            assert True
        else:
            assert False, 'fixed validations exists which is not expected for question code: ' + \
                          self.question_codes_list[i - 1] + ' Please check'

    def check_no_fixed_val_msgs(self, actual_msg, exp_msg, i):
        if actual_msg != exp_msg:
            assert True
        else:
            assert False, 'fixed validations exists which is not expected for question code: ' + \
                          self.question_codes_list[i - 1] + ' Please check'
