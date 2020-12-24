import os
import time

from base.driver_context import DriverContext
from config_files.config_test import ConfigTest


class Utilities:

    @staticmethod
    def convert_blank_data_value(data):
        if data.lower() == 'blank':
            data = ''
        elif '<Blank>' in data:
            data = data.replace('<Blank>', ' ')
        return data

    @staticmethod
    def get_values_as_a_list(values):
        return values.split(',')

    @staticmethod
    def get_question_code_element(survey, question_code):
        if survey == '023':
            question_code = question_code.replace("Q", "")
        else:
            question_code = question_code.replace("Q", "").zfill(4)
        return question_code

    @staticmethod
    def remove_multiple_spaces_in_a_string(value):
        return " ".join(value.split())

    @staticmethod
    def take_screen_shot(*scenario_details):
        scenario = scenario_details[0]
        screenshots_location = ConfigTest.HOMEDIR + '/takeon-ui/tests/acceptance-tests/screen_shots'

        scenario_error_dir = Utilities.create_screen_shots_folder(screenshots_location)
        if scenario.status.name == 'failed':
            scenario_with_line_no = scenario.feature.scenarios[0].name + '_line_no_' + str(scenario.line)

            scenario_file_path = os.path.join(scenario_error_dir,
                                              scenario_with_line_no
                                              + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                              + '.png')

            for file in os.scandir(screenshots_location):
                if scenario_with_line_no in file.name:
                    os.unlink(file.path)
                    print("remove the previous screenshot! " + file.name)
        print("take the screenshot! " + scenario_file_path)
        DriverContext.driver.save_screenshot(scenario_file_path)

    @staticmethod
    def create_screen_shots_folder(screenshots_loc):
        if not os.path.exists(screenshots_loc):
            print('create new folder')
            os.makedirs(screenshots_loc)
        return screenshots_loc
