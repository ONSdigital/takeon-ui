import os
import shutil
import time

from base.driver_context import DriverContext


class Utilities:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    SCREENSHOTS_LOC = path + '/screen_shots'

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

        if scenario.status.name == 'failed':
            Utilities.create_screen_shots_folder()
            scenario_with_line_no = scenario.feature.scenarios[0].name + '_line_no_' + str(scenario.line)

            scenario_file_path = os.path.join(Utilities.SCREENSHOTS_LOC,
                                              scenario_with_line_no
                                              + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                              + '.png')
            print("take the screenshot! " + scenario_file_path)
            DriverContext.driver.save_screenshot(scenario_file_path)

    @staticmethod
    def delete_screenshots_folder():
        if os.path.isdir(Utilities.SCREENSHOTS_LOC):
            shutil.rmtree(Utilities.SCREENSHOTS_LOC)
            print("removed the screenshots folder!")

    @staticmethod
    def create_screen_shots_folder():
        if not os.path.exists(Utilities.SCREENSHOTS_LOC):
            print('create new folder')
            os.makedirs(Utilities.SCREENSHOTS_LOC)
