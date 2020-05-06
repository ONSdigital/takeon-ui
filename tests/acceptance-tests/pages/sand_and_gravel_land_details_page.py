from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage


class SandAndGravelLandDetailsPage(BasePage):
    question_codes = {
        '601': '0601',
        '602': '0602',
        '603': '0603',
    }
    question_codes_list = ["Q601", "Q602", "Q603", "Q604", "Q605", "Q606", "Q607", 'Q608', 'Q9001']

    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    STATUS = By.XPATH, "//span[@class='status status--error']"
    QUESTION_PANEL_ERROR_MESSAGE = By.XPATH, "//div[1]/div[1]/p[1]/strong[1]"
    QUESTION_146_ELEMENT = By.ID, '0146',
    QUESTION_147_ELEMENT = By.ID, '0147',
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
    QUESTION_CODE_PANELS_ERROR_MESSAGES = By.XPATH, '//*[@id="responseForm"]/div/div/p[1]/strong'
    QUESTION_CODE_PANEL_LABEL = By.XPATH, '//*[@id="responseForm"]/div/div/p/label'

    def validate_the_previous_period_details(self, question_code, previous_value):
        self.submit_the_period_details(question_code, previous_value)
        self.driver.find_element(*SandAndGravelLandDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        SeleniumCore.close_the_current_window()

    def validate_the_current_period_details(self, question_code, current_value):
        self.driver.refresh()
        self.submit_the_period_details(question_code, current_value)
        self.driver.find_element(*SandAndGravelLandDetailsPage.SAVE_AND_VALIDATE).click()
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
        return self.driver.find_element(*SandAndGravelLandDetailsPage.STATUS).text

    def get_validation_message(self):
        return self.driver.find_element(*SandAndGravelLandDetailsPage.QUESTION_PANEL_ERROR_MESSAGE).text

    def submit_the_values_for_all_question_codes(self, existing_value, new_value):
        SeleniumCore.switch_window()
        self.submit_the_values(existing_value)
        self.save_the_application()
        self.submit_the_values(new_value)

    def save_the_application(self):
        self.driver.find_element(*SandAndGravelLandDetailsPage.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.driver.refresh()

    def submit_the_values(self, value):

        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_146_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_147_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_601_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_602_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_603_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_604_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_605_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_606_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_607_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_608_ELEMENT).send_keys(value)
        SeleniumCore.find_element_by(*SandAndGravelLandDetailsPage.QUESTION_9001_ELEMENT).send_keys(value)

    def get_the_validation_messages_for_all_question_codes(self):
        error_msg_elements = self.driver.find_elements(*SandAndGravelLandDetailsPage.QUESTION_CODE_PANELS_ERROR_MESSAGES)
        return error_msg_elements

    def get_the_fixed_validation_messages_for_all_question_codes(self):
        error_msg_elements = self.driver.find_elements(
            *SandAndGravelLandDetailsPage.QUESTION_CODE_FIXED_VALIDATION_MESSAGES)
        return error_msg_elements

    def get_all_question_codes(self):
        label_elements = self.driver.find_elements(*SandAndGravelLandDetailsPage.QUESTION_CODE_PANEL_LABEL)
        val = []
        for i in range(0, len(label_elements)):
            val.append(label_elements[i].text)
        return val
