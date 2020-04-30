# import time
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SandAndGravelLandDetails(BasePage):
    question_codes = {
        '601': '0601',
        '602': '0602',
        '603': '0603',
    }

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

    def validate_the_previous_period_details(self, question_code, previous_value):
        self.submit_the_period_details(question_code, previous_value)
        self.driver.find_element(*SandAndGravelLandDetails.SAVE_AND_VALIDATE).click()
        self.switch_to_alert_box()
        window_before = self.driver.window_handles[0]
        # close the current tab
        self.driver.close()
        self.driver.switch_to_window(window_before)
        self.driver.refresh()

    def validate_the_current_period_details(self, question_code, current_value):
        self.submit_the_period_details(question_code, current_value)
        self.driver.find_element(*SandAndGravelLandDetails.SAVE_AND_VALIDATE).click()
        self.switch_to_alert_box()
        self.driver.refresh()

    def submit_the_period_details(self, question_code, value):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        question_code_ele = self.driver.find_element_by_id(self.get_question_codes(question_code))
        question_code_ele.clear()
        question_code_ele.send_keys(value)

    def get_question_codes(self, question_code):
        return self.question_codes[question_code]

    def check_threshold_value(self, previous_value, current_value, threshold_value):
        result_value = int(current_value) - int(previous_value)
        if result_value > int(threshold_value):
            return 'true'
        else:
            return 'false'

    def get_status(self, status_type):
        return self.driver.find_element(*SandAndGravelLandDetails.STATUS).text

    def get_validation_message(self):
        return self.driver.find_element(*SandAndGravelLandDetails.QUESTION_PANEL_ERROR_MESSAGE).text

    def switch_to_alert_box(self):
        # Click on the "Refresh" button to generate the Confirmation Alert
        self.driver.refresh()
        try:
            # Switch the control to the Alert window
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alert')
            alert = self.driver.switch_to.alert
            # Retrieve the message on the Alert window
            message = alert.text
            print("Alert shows following message: " + message)
            time.sleep(2)
            # use the accept() method to accept the alert
            alert.accept()
            print("Alert accepted")
            # get the text returned when OK Button is clicked.
            txt = self.driver.find_element_by_id('msg')
            print(txt.text)
            time.sleep(2)
        except TimeoutException:
            print("No Alert")
