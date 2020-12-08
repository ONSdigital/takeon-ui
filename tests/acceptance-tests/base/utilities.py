import os
import time

from base.driver_context import DriverContext


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
    def take_screen_shot(*scenario):
        scenario_error_dir = Utilities.create_screen_shots_folder(scenario[1])
        if scenario[0].status.name == 'failed':
            scenario_file_path = os.path.join(scenario_error_dir,
                                              scenario[0].feature.scenarios[0].name + '_line_no_' +
                                              str(scenario[0].line)
                                              + '_' + time.strftime("%d_%m_%Y")
                                              + '.png')
            print("getting the screenshot!")
            DriverContext.driver.save_screenshot(scenario_file_path)

    @staticmethod
    def create_screen_shots_folder(screenshots_loc):

        if not os.path.exists(screenshots_loc):
            print('create new folder')
            os.makedirs(screenshots_loc)
        else:
            # specify the days from which the files to be deleted
            days = 1
            # converting days to seconds
            seconds = time.time() - (days * 24 * 60 * 60)
            ctime = os.stat(screenshots_loc).st_ctime
            # comparing the days
            if seconds >= ctime:
                Utilities.delete_all_the_previous_screenshots(screenshots_loc)
            print('No need to create new folder')
        return screenshots_loc

    @staticmethod
    def delete_all_the_previous_screenshots(folder_path):
        for file in os.scandir(folder_path):
            if file.name.endswith(".png"):
                os.unlink(file.path)
