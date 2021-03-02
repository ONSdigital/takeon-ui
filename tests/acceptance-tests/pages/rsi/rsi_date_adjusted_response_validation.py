from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.check_messages_contributor_details import CheckMessagesContributorDetails
from pages.common.contributor_details.check_values_contributor_details import CheckValuesContributorDetails
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.common.contributor_details_page import ContributorDetailsPage
from pages.locators import contributor_details


class RsiDateAdjustedResponseValidation(ContributorDetailsPage):
    PERIOD_START_DATE_ELEMENT = '11'
    PERIOD_END_DATE_ELEMENT = '12'
    period = ''
    start_date = ''
    end_date = ''

    def set_period_start_date(self, value):
        SeleniumCore.set_current_data_text(self.PERIOD_START_DATE_ELEMENT, value)

    def set_period_end_date(self, value):
        SeleniumCore.set_current_data_text(self.PERIOD_END_DATE_ELEMENT, value)

    def submit_period_dates(self, period, start_date, end_date):
        RsiDateAdjustedResponseValidation.period = period
        RsiDateAdjustedResponseValidation.start_date = Utilities.convert_blank_data_value(start_date)
        RsiDateAdjustedResponseValidation.end_date = Utilities.convert_blank_data_value(end_date)
        self.set_period_start_date(RsiDateAdjustedResponseValidation.start_date)
        self.set_period_end_date(RsiDateAdjustedResponseValidation.end_date)

    def check_adjusted_responses(self, *responses):
        self.date_range = responses[0]
        self.actual_response_values = Utilities.get_values_as_a_list(responses[1])
        self.expected_response_type = Utilities.get_values_as_a_list(responses[2])[0]

        total_turnover = self.get_adjusted_response('Q20')
        internet_sales = self.get_adjusted_response('Q21')

        expected_response_type = Utilities.convert_blank_data_value(self.expected_response_type)
        t_turnover = Utilities.convert_blank_data_value(self.compare_values(total_turnover, 0))
        i_sales = Utilities.convert_blank_data_value(self.compare_values(internet_sales, 1))

        ReportingHelper.check_single_message_matches('Q21', t_turnover, expected_response_type)

        ReportingHelper.check_single_message_matches('Q20', i_sales, expected_response_type)

    def get_adjusted_response(self, question_code):

        question_row = GetContributorDetails().get_question_code_row_details(
            contributor_details.CURRENT_DATA_TAB_ELEMENT, question_code)
        element = contributor_details.ADJUSTED_RESPONSE_COLUMN + contributor_details.ERROR_LABEL
        adjusted_response = question_row.find_element(By.XPATH, element).text
        return adjusted_response

    def get_adjusted_internet_sales_response(self):
        return SeleniumCore.get_attribute_element_text(By.ID, '21')

    def compare_values(self, adjusted_response, i):
        period = RsiDateAdjustedResponseValidation.period
        start_date = RsiDateAdjustedResponseValidation.start_date
        end_date = RsiDateAdjustedResponseValidation.end_date

        actual_days_returned = 25
        if period == '201903' and period in start_date and period in end_date and adjusted_response != '':

            if start_date <= end_date:
                no_of_days_returned = abs((int(end_date) - int(start_date))) + 1
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
            
        else:
            return "blank"
