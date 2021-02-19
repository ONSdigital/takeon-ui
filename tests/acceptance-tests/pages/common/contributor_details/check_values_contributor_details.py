import time

from base.driver_context import DriverContext
from base.reporting_helper import ReportingHelper
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from pages.common.contributor_details.check_messages_contributor_details import CheckMessagesContributorDetails
from pages.common.contributor_details.get_contributor_details import GetContributorDetails
from pages.locators import contributor_details


class CheckValuesContributorDetails:

    def check_if_validation_status_changed(self):
        i = 0
        while i < 6:
            status = GetContributorDetails().get_validation_status().lower()

            if status == 'check needed':
                if i > 0:
                    break
                self.refresh_the_form()
            elif status != 'check needed':
                self.refresh_the_form()
            i += 1

    def refresh_the_form(self):
        DriverContext.driver.refresh()
        time.sleep(2)

    def save_the_application(self):
        DriverContext.driver.find_element(
            *contributor_details.SAVE_AND_VALIDATE).click()
        SeleniumCore.switch_to_alert_box()
        self.check_if_validation_status_changed()

    def check_values_are_not_equal(self, question, comparison_val_one, comparison_val_two, result):
        CheckMessagesContributorDetails().check_if_overall_validation_triggered()
        if comparison_val_one == 'blank' and comparison_val_two == 'blank':
            comparison_val_one = Utilities.convert_blank_data_value(comparison_val_one)
            comparison_val_two = Utilities.convert_blank_data_value(comparison_val_two)
            is_validation_exists = ReportingHelper.compare_strings(comparison_val_one,
                                                                   comparison_val_two)

        else:
            is_validation_exists = ReportingHelper.compare_values_are_not_equal(comparison_val_one,
                                                                                comparison_val_two)
        ReportingHelper.check_single_message_matches(
            question, result, str(is_validation_exists).lower())

    def check_values_movement_to_or_from_zero(self, question_codes, comparison_val_one, comparison_val_two, result):
        CheckMessagesContributorDetails().check_if_overall_validation_triggered()
        if len(question_codes) > 1:
            for question in question_codes:
                if comparison_val_one == 'blank' and comparison_val_two == 'blank':
                    value_one = Utilities.convert_blank_data_value(comparison_val_one)
                    value_two = Utilities.convert_blank_data_value(comparison_val_two)
                    is_validation_exists = ReportingHelper.compare_strings(value_one,
                                                                           value_two)

                else:
                    is_validation_exists = ReportingHelper.compare_the_zero_movement_values(comparison_val_one,
                                                                                            comparison_val_two)
                ReportingHelper.check_single_message_matches(
                    question, result, str(is_validation_exists).lower())
