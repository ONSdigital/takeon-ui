from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.common.base_page import BasePage
from pages.common.contributor_details_page import ContributorDetailsPage


class TestSurveyContributorDetailsPage(BasePage):
    QUESTION_ONE_ELEMENT = By.ID, '1000'
    QUESTION_TWO_ELEMENT = By.ID, '1001'
    QUESTION_DERIVED_ELEMENT = By.ID, '4001'
    COMMENT_QUESTION_NOT_BLANK = By.ID, '5000'
    COMMENT_QUESTION_VALUE = By.ID, '5001'
    ERROR_MESSAGE_ELEMENT_STRING_PART_ONE = '//strong[contains(text(),"'
    ERROR_MESSAGE_ELEMENT_STRING_PART_TWO = '")]'
    QUESTION_LABEL_PART_ONE = "//label[contains(text(),'"
    QUESTION_LABEL_PART_TWO = "')]"

    def set_internet_sales_value(self, value):
        SeleniumCore.set_element_text(*TestSurveyContributorDetailsPage.QUESTION_TWO_ELEMENT, value)

    def set_total_turnover_sales_value(self, value):
        SeleniumCore.set_element_text(*TestSurveyContributorDetailsPage.QUESTION_ONE_ELEMENT, value)

    def submit_pp_sales_values(self, internet_sales, total_sales):
        SeleniumCore.switch_window()
        self.pp_internet_sales = internet_sales
        self.pp_total_sales = total_sales
        self.set_internet_sales_value(internet_sales)
        self.set_total_turnover_sales_value(total_sales)
        ContributorDetailsPage().save_the_application()
        SeleniumCore.close_the_current_window()

    def validate_the_current_period_details(self, internet_sales):
        SeleniumCore.switch_window()
        self.set_internet_sales_value(internet_sales)
        ContributorDetailsPage().save_the_application()

    def run_the_validation_process(self, ques_val_1, ques_val_2):
        SeleniumCore.switch_window()
        SeleniumCore.set_element_text(*TestSurveyContributorDetailsPage.QUESTION_ONE_ELEMENT, ques_val_1)
        SeleniumCore.set_element_text(*TestSurveyContributorDetailsPage.QUESTION_TWO_ELEMENT, ques_val_2)
        ContributorDetailsPage().save_the_application()

    def get_derived_question_value(self):
        return int(SeleniumCore.get_attribute_element_text(*TestSurveyContributorDetailsPage.QUESTION_DERIVED_ELEMENT))

    def check_threshold_value(self):
        if int(self.pp_internet_sales) > 0.1 * int(self.pp_total_sales):
            return False

    def check_validation_message(self):
        element_text = "This value is 0. Previous period it was more than a certain percentage of the total."
        element = self.ERROR_MESSAGE_ELEMENT_STRING_PART_ONE + element_text + self.ERROR_MESSAGE_ELEMENT_STRING_PART_TWO
        if len(self.driver.find_elements_by_xpath(element)) > 0:
            return True
        else:
            return False



    def submit_comment_value(self, comment, question):
        SeleniumCore.switch_window()
        if comment.lower() == 'empty' or comment.lower() == 'blank':
            comment = ''
        if question.upper() == 'Q7':
            SeleniumCore.set_element_text(*TestSurveyContributorDetailsPage.COMMENT_QUESTION_NOT_BLANK, comment)
        if question.upper() == 'Q8':
            SeleniumCore.set_element_text(*TestSurveyContributorDetailsPage.COMMENT_QUESTION_VALUE, comment)
