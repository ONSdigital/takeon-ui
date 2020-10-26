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
        scenario_error_dir = Utilities.create_screen_shots_folder()
        if scenario[0].status.name == 'failed':
            # the element with longest height on page
            scenario_file_path = os.path.join(scenario_error_dir,
                                              scenario[0].feature.scenarios[0].name
                                              + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                              + '.png')
            el = DriverContext.driver.find_element_by_tag_name('body')
            el.screenshot(scenario_file_path)

    @staticmethod
    def create_screen_shots_folder():
        scenario_error_dir = os.path.expanduser("~") + '/takeon-ui/tests/acceptance-tests/screen_shots'
        if not os.path.exists(scenario_error_dir):
            os.makedirs(scenario_error_dir)
        else:
            Utilities.delete_all_the_previous_screenshots(scenario_error_dir)
        return scenario_error_dir

    @staticmethod
    def delete_all_the_previous_screenshots(folder_path):
        for file in os.scandir(folder_path):
            if file.name.endswith(".png"):
                os.unlink(file.path)

    @staticmethod
    def get_current_page_title():
        return DriverContext.driver.find_element_by_xpath("//div[contains(@class,'header__title')]").text

    @staticmethod
    def check_page_title(page_title):
        current_title = Utilities.get_current_page_title()
        if current_title.lower() != page_title.lower():
            assert False, 'Expected page header title to be "' + page_title + '" But the current page header title is "' + current_title + '"'
