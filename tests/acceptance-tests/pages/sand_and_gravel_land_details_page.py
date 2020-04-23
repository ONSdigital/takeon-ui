# import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class ContributionDetailsPage(BasePage):
    question_codes = {
        '601': '0601',
        '602': '0602',
        '603': '0603',
    }

    SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
    STATUS = By.CLASS_NAME, 'status status--success'
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

    def validate_the_period_details(self, question_code, value):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        question_code_ele = self.driver.find_element_by_id(self.get_question_codes(question_code))
        question_code_ele.send_keys(value)

    def get_question_codes(self, question_code):
        return self.question_codes[question_code]

    def check_status(self):
        status = self.driver.find_element(*ContributionDetailsPage.STATUS)
        assert status.text == 'Clear'
