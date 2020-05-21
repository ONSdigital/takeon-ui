from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage


class ContributorDetailsPage(BasePage):
    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    NO_OF_QUESTIONS = By.XPATH, "//p[@class='field']"
    QUESTION_CODE_PANEL_CLASS_ELEMENTS = By.XPATH, "//div[@class='panel panel--error panel--simple']"
    Q_CODE_VALIDATION_ONE = '//div[@class="panel panel--error panel--simple"]//label[contains(text(),"'
    NO_OF_VALIDATION_ELEMENTS = '//*[@id="responseForm"]/div/div/p/strong'
    Q_CODE_PART_ONE = '//*[@id="responseForm"]/div['
    Q_CODE_PART_TWO = ']/div/p/strong'
    Q_CODE_PART_THREE = ']/div//label[contains(text(),"'
    Q_CODE_PART_FOUR = '")]'
    Q_CODE_LABELS_WITH_TEXT = "//label[contains(text(),'"
    QUESTION_CODE_ERROR_MESSAGES_PART_ONE = By.XPATH, "//div["
    QUESTION_CODE_ERROR_MESSAGES_PART_TWO = By.XPATH, "]/div/p[@class='panel__error u-mb-no']"
    STATUS = By.XPATH, "//span[@class='status status--error']"
    QUESTION_PANEL_ERROR_MESSAGE = By.XPATH, "//div[1]/div[1]/p[1]/strong[1]"
    QUESTION_CODE_FIXED_VALIDATION_MESSAGES = By.XPATH, '//*[@id="responseForm"]/div/div/p[2]/strong'

    def save_the_application(self):
        self.driver.find_element(*ContributorDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.driver.refresh()

    def check_numeric_fixed_validation(self, questions_list, is_validation_exists):
        # iterate through the list of expected question codes
        for q in questions_list:
            question_validation_ele = self.Q_CODE_VALIDATION_ONE + q + self.Q_CODE_PART_FOUR
            # check if any validation exists for a question
            if len(self.driver.find_elements_by_xpath(question_validation_ele)) > 0:
                error_elements = self.driver.find_elements_by_xpath(self.NO_OF_VALIDATION_ELEMENTS)
                for error_element in error_elements:
                    if error_element.text == 'Value set to default, please check':
                        assert False
            else:
                assert is_validation_exists == 'not'

    def check_fixed_validation_messages(self, survey, question_codes_list, is_validation_exists, i, no_of_error_msgs,
                                        actual_msg):
        if survey == '0074':
            if question_codes_list[i - 1] != 'Q8000':
                self.check_validation_messages(question_codes_list, is_validation_exists, i, no_of_error_msgs,
                                               actual_msg)
        elif survey == '0073':
            self.check_validation_messages(question_codes_list, is_validation_exists, i, no_of_error_msgs, actual_msg)

        else:
            self.check_validation_messages(question_codes_list, is_validation_exists, i, no_of_error_msgs, actual_msg)

    def check_validation_messages(self, question_codes_list, is_validation_exists, i, no_of_error_msgs, actual_msg):

        if is_validation_exists == 'be':
            if len(no_of_error_msgs) == 1:
                self.check_fixed_val_msgs(question_codes_list, actual_msg, no_of_error_msgs[0].text, i)
            elif len(no_of_error_msgs) == 2:
                self.check_fixed_val_msgs(question_codes_list, actual_msg, no_of_error_msgs[1].text, i)
            elif len(no_of_error_msgs) == 0:
                print("No validation exists for the question code: " + question_codes_list[i - 1])

        elif is_validation_exists == 'not be':
            if len(no_of_error_msgs) == 1:
                self.check_no_fixed_val_msgs(question_codes_list, actual_msg, no_of_error_msgs[0].text, i)
            elif len(no_of_error_msgs) == 2:
                self.check_no_fixed_val_msgs(question_codes_list, actual_msg, no_of_error_msgs[1].text, i)
            elif len(no_of_error_msgs) == 0:
                print("No validation exists for the question code: " + question_codes_list[i - 1])

    def check_fixed_val_msgs(self, question_codes_list, actual_msg, exp_msg, i):
        if actual_msg == exp_msg:
            assert True
        else:
            assert False, 'Fixed validation did not exist - expected message: "' + exp_msg + \
                          '" did not match with the actual message : "' + actual_msg + '" for question code: ' + \
                          question_codes_list[i - 1]

    def check_no_fixed_val_msgs(self, question_codes_list, actual_msg, exp_msg, i):
        if actual_msg != exp_msg:
            assert True
        else:
            assert False, 'fixed validations exists which is not expected for question code: ' + \
                          question_codes_list[i - 1] + ' Please check'
