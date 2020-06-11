from selenium.webdriver.common.by import By

from base.selenium_core import SeleniumCore
from pages.base_page import BasePage
from pages.contributor_details_page import ContributorDetailsPage


class TestSurveyContributorDetailsPage(BasePage):
    QUESTION_ONE_ELEMENT = By.ID, '1000'
    QUESTION_TWO_ELEMENT = By.ID, '1001'
    ERROR_MESSAGE_ELEMENT_STRING_PART_ONE = '//strong[contains(text(),"'
    ERROR_MESSAGE_ELEMENT_STRING_PART_TWO = '")]'

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