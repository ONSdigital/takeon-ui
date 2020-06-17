from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.common.base_page import BasePage
from pages.common.contributor_details_page import ContributorDetailsPage


class RsiContributorDetailsPage(BasePage):
    QUESTION_ONE_ELEMENT = By.ID, '0020'
    QUESTION_TWO_ELEMENT = By.ID, '0021'
    QUESTION_NO_146 = By.ID, '0146'
    QUESTION_LABEL_PART_ONE = "//label[contains(text(),'"
    QUESTION_LABEL_PART_TWO = "')]"
    QUESTION_DERIVED_ELEMENT = '7034'

    def set_internet_sales_value(self, value):
        SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_TWO_ELEMENT, value)

    def set_total_turnover_sales_value(self, value):
        SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_ONE_ELEMENT, value)

    def submit_pp_sales_values(self, internet_sales, total_sales):
        SeleniumCore.switch_window()
        self.pp_internet_sales = internet_sales
        self.pp_total_sales = total_sales
        self.set_internet_sales_value(internet_sales)
        self.set_total_turnover_sales_value(total_sales)
        ContributorDetailsPage().save_the_application()
        SeleniumCore.close_the_current_window()

    def submit_comment_value(self, comment, question):
        SeleniumCore.switch_window()
        if comment == 'empty':
            comment = ''
        if question.upper() == 'Q146':
            SeleniumCore.set_element_text(*RsiContributorDetailsPage.QUESTION_NO_146, comment)

    def validate_the_current_period_details(self, internet_sales):
        SeleniumCore.switch_window()
        self.set_internet_sales_value(internet_sales)
        ContributorDetailsPage().save_the_application()

    def check_threshold_value(self):
        if int(self.pp_internet_sales) > 0.1 * int(self.pp_total_sales):
            return False

    def check_validation_message(self):
        exp_msg = "This value is 0. Previous period it was more than a certain percentage of the total."
        actual_msg = ContributorDetailsPage().get_validation_error_message('Q21')
        if exp_msg == actual_msg:
            return True
        else:
            return False

    def check_comment_present_val_msg(self, exp_msg, is_val_exists):
        ContributorDetailsPage().check_validation_message('Q146', exp_msg, is_val_exists)
    
    def get_derived_question_value(self):
        return int(SeleniumCore.get_attribute_element_text(*TestSurveyContributorDetailsPage.QUESTION_DERIVED_ELEMENT))
