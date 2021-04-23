from selenium.webdriver.common.by import By

from base.reporting_helper import ReportingHelper
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
        if len(responses) > 2:
            self.expected_response_type = Utilities.get_values_as_a_list(responses[3])[0]
        questions_list = responses[1]
        count = 0
        if len(questions_list) > 1 and type(questions_list) == list:
            for question in questions_list:
                self.actual_response_values = Utilities.get_values_as_a_list(responses[2])[count]
                question_one_value = self.get_adjusted_response(question)
                question_one = self.compare_values(question_one_value, 0)
                ReportingHelper.check_single_message_matches(question,
                                                             question_one,
                                                             self.expected_response_type)
                count += 1
        else:
            question_one_value = self.get_adjusted_response(questions_list)
            question_one = self.compare_values(question_one_value, 0)
            ReportingHelper.check_single_message_matches(questions_list,
                                                         question_one,
                                                         'blank')

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

        if start_date != '' and end_date != '' and adjusted_response != '':

            if self.start_date <= self.end_date:
                # no_of_days_returned = abs((int(self.end_date) - int(self.start_date))) + 1
                act_response = float(self.actual_response_values[i])
                adj_response = float(adjusted_response)

                if adj_response > act_response:
                    return "increased"
                elif adj_response < act_response:
                    return "decreased"
        elif adjusted_response != '':
            if float(adjusted_response) > float(
                    self.actual_response_values[i]):
                return "increased"
        else:
            return "blank"

    def check_adjusted_response_for_derived_question(self, *responses):
        self.check_adjusted_responses(responses)