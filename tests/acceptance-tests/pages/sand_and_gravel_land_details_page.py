from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage


class SandGravelLandAndMarineDetailsPage(BasePage):
    question_codes = {
        '601': '0601',
        '602': '0602',
        '603': '0603',
    }
    question_codes_list = ["Q601", "Q602", "Q603", "Q604", "Q605", "Q606", "Q607", 'Q608']
    land_numeric_question_codes_list = ["Q146", "Q147"]
    marine_numeric_question_codes_list = ["Q146", "Q148"]

    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    STATUS = By.XPATH, "//span[@class='status status--error']"
    QUESTION_PANEL_ERROR_MESSAGE = By.XPATH, "//div[1]/div[1]/p[1]/strong[1]"
    QUESTION_146_ELEMENT = By.ID, '0146',
    QUESTION_147_ELEMENT = By.ID, '0147',
    QUESTION_148_ELEMENT = By.ID, '0148',
    QUESTION_601_ELEMENT = By.ID, '0601',
    QUESTION_602_ELEMENT = By.ID, '0602',
    QUESTION_603_ELEMENT = By.ID, '0603',
    QUESTION_604_ELEMENT = By.ID, '0604',
    QUESTION_605_ELEMENT = By.ID, '0605',
    QUESTION_606_ELEMENT = By.ID, '0606',
    QUESTION_607_ELEMENT = By.ID, '0607',
    QUESTION_608_ELEMENT = By.ID, '0608',
    QUESTION_9001_ELEMENT = By.ID, '9001',
    QUESTION_CODE_FIXED_VALIDATION_MESSAGES = By.XPATH, '//*[@id="responseForm"]/div/div/p[2]/strong'
    QUESTION_CODE_PANELS_ERROR_MESSAGES = By.XPATH, '//*[@id="responseForm"]/div/div/p/strong'
    QUESTION_CODE_PANEL_LABEL = By.XPATH, '//*[@id="responseForm"]/div/div/p/label'

    # QUESTION_CODE_ELEMENTS_PART_FIXED_MSG = ']/div/p[2]/strong'
    # QUESTION_CODE_ELEMENTS_PART_THREE = ']/div/p[2]'
    # QUESTION_CODE_ELEMENTS_PART_FOUR = ']/div/p[3]'
    # QUESTION_ONE = '//label[contains(text(),'

    QUESTION_CODE_PANEL_CLASS_ELEMENTS = By.XPATH, "//p[@class='panel__error u-mb-no']"
    QCODE_VALIDATION_ONE = '//div[@class="panel panel--error panel--simple"]//label[contains(text(),"'
    Q_CODE_PART_ONE = '//*[@id="responseForm"]/div['
    Q_CODE_PART_TWO = ']/div/p/strong'
    Q_CODE_PART_THREE = ']/div//label[contains(text(),"'
    Q_CODE_PART_FOUR = '")]'
    Q_CODE_LABELS_WITH_TEXT = "//label[contains(text(),'"

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
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_147_ELEMENT).send_keys(value)
        self.submit_the_common_survey_values(value)

    def submit_the_marine_survey_values(self, value):
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_148_ELEMENT).send_keys(value)
        self.submit_the_common_survey_values(value)

    def submit_the_common_survey_values(self, value):
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_146_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_601_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_602_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_603_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_604_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_605_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_606_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_607_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_608_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandGravelLandAndMarineDetailsPage.QUESTION_9001_ELEMENT).send_keys(value)

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
            question_validation_ele = self.QCODE_VALIDATION_ONE + questions_list[
                i] + self.Q_CODE_PART_FOUR
            # check if any validation exists for a question
            if len(self.driver.find_elements_by_xpath(question_validation_ele)) > 0:
                assert False
            else:
                assert is_validation_exists == 'not'

    def check_fixed_validations_exists(self, validation_message, is_validation_exists):

        i = 0
        # iterate through the list of expected question codes
        while i < len(self.question_codes_list):
            question_validation_ele = self.QCODE_VALIDATION_ONE + self.question_codes_list[
                i] + self.Q_CODE_PART_FOUR

            # check if any validation exists for a question
            if len(self.driver.find_elements_by_xpath(question_validation_ele)) > 0:

                # get the number of validation groups exists for all questions
                elements = self.driver.find_elements(*SandGravelLandAndMarineDetailsPage.QUESTION_CODE_PANEL_CLASS_ELEMENTS)
                for j in range(0, len(elements)):
                    error_element = self.Q_CODE_PART_ONE + str(j + 1) + self.Q_CODE_PART_TWO
                    no_of_error_messages_per_question = self.driver.find_elements_by_xpath(error_element)

                    # check if there are more than one validation exists for the question
                    if len(no_of_error_messages_per_question) == 2:
                        question_element = self.Q_CODE_PART_ONE + str(j + 1) + self.Q_CODE_PART_THREE + \
                                           self.question_codes_list[i] + self.Q_CODE_PART_FOUR
                        question_ele = self.driver.find_element_by_xpath(question_element)

                        # check right question has the validation
                        if self.question_codes_list[i] in question_ele.text:
                            if validation_message in elements[1].text:
                                assert is_validation_exists == 'be'
                                i += 1
                            else:
                                assert False

                    # check if there are more than one validation exists for the question
                    if len(no_of_error_messages_per_question) == 1:
                        question_element = self.Q_CODE_PART_ONE + str(
                            j + 1) + self.Q_CODE_PART_THREE + \
                                           self.question_codes_list[i] + self.Q_CODE_PART_FOUR
                        question_ele = self.driver.find_element_by_xpath(question_element)

                        # check right question has the validation
                        if self.question_codes_list[i] in question_ele.text:
                            if validation_message not in elements[0].text:
                                assert is_validation_exists == 'not be'
                                i += 1
                            else:
                                assert False
            else:
                i += 1
