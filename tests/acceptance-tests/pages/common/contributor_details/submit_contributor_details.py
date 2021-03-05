from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.locators import contributor_details


class SubmitContributorDetails:

    def submit_question_value(self, period, survey, value_type, value, question):
        if value_type:
            self.submit_sales_value(period, survey, value, question)

    def submit_sales_value(self, period, survey, value, question):
        value = Utilities.convert_blank_data_value(value)
        question_element = Utilities.get_question_code_element(survey, question)
        self.submit_default_period_dates(period)
        SeleniumCore.set_current_data_text(question_element, value)

    def submit_values_for_survey_questions(self, questions_and_values):
        period = questions_and_values[0]
        self.submit_default_period_dates(period)
        survey = questions_and_values[1]
        questions_list = questions_and_values[2]
        commodity_values = Utilities.get_values_as_a_list(questions_and_values[3])

        if len(commodity_values) > 1 and type(questions_list) == list:
            self.submit_values_as_a_list_for_multiple_questions(survey, questions_list, commodity_values)
        elif len(commodity_values) == 1 and type(questions_list) == list:
            self.submit_single_value_for_multiple_questions(survey, questions_list, commodity_values[0])
        else:
            self.submit_single_value_per_question(survey, questions_list, commodity_values[0])

    def submit_values_as_a_list_for_multiple_questions(self, survey, questions_list, commodity_values):
        if len(questions_list) > 1:
            count = 0
        for question in questions_list:
            question_element = Utilities.get_question_code_element(survey, question)
            SeleniumCore.set_current_data_text(
                question_element, Utilities.convert_blank_data_value(commodity_values[count]))
            if len(commodity_values) > 1:
                count += 1

    def submit_single_value_for_multiple_questions(self, survey, questions_list, commodity_value):
        for question in questions_list:
            question_element = Utilities.get_question_code_element(survey, question)
            commodity_value = Utilities.convert_blank_data_value(commodity_value)
            SeleniumCore.set_current_data_text(question_element, commodity_value)

    def submit_single_value_per_question(self, survey, questions_list, commodity_value):
        question_element = Utilities.get_question_code_element(survey, questions_list)
        SeleniumCore.set_current_data_text(
            question_element, commodity_value)

    def set_period_start_date(self, value):
        SeleniumCore.set_current_data_text(contributor_details.PERIOD_START_DATE_ELEMENT, value)

    def set_period_end_date(self, value):
        SeleniumCore.set_current_data_text(contributor_details.PERIOD_END_DATE_ELEMENT, value)

    def submit_period_dates(self, start_date=None, end_date=None):
        if start_date or end_date is not None:
            st_date = Utilities.convert_blank_data_value(start_date)
            en_date = Utilities.convert_blank_data_value(end_date)
            self.set_period_start_date(st_date)
            self.set_period_end_date(en_date)
        else:
            self.submit_default_period_dates()

    def submit_default_period_dates(self, period):
        if period == '201903':
            self.set_period_start_date('20190304')
            self.set_period_end_date('20190328')
        elif period == '201904':
            self.set_period_start_date('20190404')
            self.set_period_end_date('20190428')
        else:
            assert False, 'Period do not match the expected period: ' + period
