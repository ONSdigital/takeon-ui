from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage


class BricksSurveyDetailsPage(BasePage):
    QUESTION_CODES = [
        (By.ID, '0001'), (By.ID, '0002'), (By.ID, '0003'), (By.ID, '0004'),
        (By.ID, '0011'), (By.ID, '0012'), (By.ID, '0013'), (By.ID, '0014'),
        (By.ID, '0021'), (By.ID, '0022'), (By.ID, '0023'), (By.ID, '0024'),
        (By.ID, '0145'), (By.ID, '0146'), (By.ID, '0501'), (By.ID, '0502'),
        (By.ID, '0503'), (By.ID, '0504'), (By.ID, '8000'), (By.ID, '9204'),
        (By.ID, '9214'), (By.ID, '9224'), (By.ID, '9501'), (By.ID, '9502'),
        (By.ID, '9503'), (By.ID, '9504')]

    question_codes_list = [
        'Q001', 'Q002', 'Q003', 'Q004', 'Q011', 'Q012', 'Q013', 'Q014', 'Q021', 'Q022', 'Q023', 'Q024',
        'Q501', 'Q502', 'Q503', 'Q504', 'Q8000', 'Q9204', 'Q9214', 'Q9224', 'Q9501', 'Q9502', 'Q9503', 'Q9504']

    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    NO_OF_QUESTIONS = By.XPATH, "//p[@class='field']"
    QUESTION_CODE_PANEL_CLASS_ELEMENTS = By.XPATH, "//div[@class='panel panel--error panel--simple']"
    QCODE_VALIDATION_ONE = '//div[@class="panel panel--error panel--simple"]//label[contains(text(),"'
    Q_CODE_PART_ONE = '//*[@id="responseForm"]/div['
    Q_CODE_PART_TWO = ']/div/p/strong'
    Q_CODE_PART_THREE = ']/div//label[contains(text(),"'
    Q_CODE_PART_FOUR = '")]'
    Q_CODE_LABELS_WITH_TEXT = "//label[contains(text(),'"
    QUESTION_CODE_ERROR_MESSAGES_PART_ONE = By.XPATH, "//div["
    QUESTION_CODE_ERROR_MESSAGES_PART_TWO = By.XPATH, "]/div/p[@class='panel__error u-mb-no']"

    def submit_the_values_for_bricks_survey_question_codes(self, existing_value, new_value):
        SeleniumCore.switch_window()
        self.submit_the_bricks_question_values(existing_value)
        self.save_the_application()
        self.submit_the_bricks_question_values(new_value)

    def submit_the_bricks_question_values(self, value):
        for question in self.QUESTION_CODES:
            SeleniumCore.find_element_by(*question).send_keys(value)

    def save_the_application(self):
        self.driver.find_element(*BricksSurveyDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.driver.refresh()

    def check_fixed_validations_exists(self, validation_message, is_validation_exists):

        count = 0
        # get the number of validation message groups exists for all questions
        elements = self.driver.find_elements(*BricksSurveyDetailsPage.QUESTION_CODE_PANEL_CLASS_ELEMENTS)
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
            elif len(no_of_error_msgs) == 2 and self.question_codes_list[i - 1] != 'Q8000':
                self.check_fixed_val_msgs(actual_msg, no_of_error_msgs[1].text, i)
            elif len(no_of_error_msgs) == 0:
                print("No validation exists for the question code: " + self.question_codes_list[i - 1])

        elif is_validation_exists == 'not be':
            if len(no_of_error_msgs) == 1:
                self.check_no_fixed_val_msgs(actual_msg, no_of_error_msgs[0].text, i)
            elif len(no_of_error_msgs) == 2 and self.question_codes_list[i - 1] != 'Q8000':
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
