from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.common.contributor_details.submit_contributor_details import SubmitContributorDetails
from pages.common.contributor_details_page import ContributorDetailsPage
from pages.locators import contributor_details


class RsiDateAdjustedResponseValidation(ContributorDetailsPage):
    end_date = None
    start_date = None
    period = None

    def submit_period_dates(self, period, start_date, end_date):
        RsiDateAdjustedResponseValidation.period = period
        RsiDateAdjustedResponseValidation.start_date = Utilities.convert_blank_data_value(start_date)
        RsiDateAdjustedResponseValidation.end_date = Utilities.convert_blank_data_value(end_date)
        SubmitContributorDetails().submit_period_dates(RsiDateAdjustedResponseValidation.start_date,
                                                       RsiDateAdjustedResponseValidation.end_date)

    def check_adjusted_responses(self, *responses):
        self.actual_response_values = Utilities.get_values_as_a_list(responses[1])
        self.expected_response_type = Utilities.get_values_as_a_list(responses[2])[0]

        total_turnover = self.get_adjusted_response(contributor_details.TOTAL_TURNOVER_QUESTION_ELEMENT)
        internet_sales = self.get_adjusted_response(contributor_details.INTERNET_SALES_QUESTION_ELEMENT)

        t_turnover = self.compare_values(total_turnover, 0)
        i_sales = self.compare_values(internet_sales, 1)

        ReportingHelper.check_single_message_matches(contributor_details.TOTAL_TURNOVER_QUESTION_ELEMENT, t_turnover,
                                                     self.expected_response_type)

        ReportingHelper.check_single_message_matches(contributor_details.INTERNET_SALES_QUESTION_ELEMENT, i_sales,
                                                     self.expected_response_type)

    def get_adjusted_response(self, question_code):

        question_row = GetContributorDetails().get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question_code)
        element = contributor_details.ADJUSTED_RESPONSE_COLUMN + contributor_details.ERROR_LABEL
        adjusted_response = question_row.find_element(By.XPATH, element).text
        return adjusted_response

    def compare_values(self, adjusted_response, i):
        period = RsiDateAdjustedResponseValidation.period
        start_date = RsiDateAdjustedResponseValidation.start_date
        end_date = RsiDateAdjustedResponseValidation.end_date

        actual_days_returned = 25
        if period == '201903' and start_date != '' and end_date != '' and adjusted_response != '':

            if self.start_date <= self.end_date:
                no_of_days_returned = abs((int(self.end_date) - int(self.start_date))) + 1
                act_response = float(self.actual_response_values[i])
                adj_response = float(adjusted_response)

                if no_of_days_returned == actual_days_returned and adj_response == act_response:
                    return "same"
                elif no_of_days_returned < actual_days_returned and adj_response > act_response:
                    return "increased"
                elif no_of_days_returned > actual_days_returned:
                    return "blank"

        elif period == '201903' and start_date == '' and end_date == '':
            if float(adjusted_response) == float(
                    self.actual_response_values[i]):
                return "same"
        elif period == '201903' and adjusted_response != '':
            if float(adjusted_response) > float(
                    self.actual_response_values[i]):
                return "increased"
            elif float(adjusted_response) == float(
                    self.actual_response_values[i]):
                return "same"
        else:
            return "blank"
