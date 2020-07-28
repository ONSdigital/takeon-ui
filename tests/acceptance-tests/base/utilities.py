class Utilities:

    @staticmethod
    def convert_blank_data_to_empty_string(data):
        if data.lower() == 'blank':
            data = ''
        return data

    @staticmethod
    def replace_blank_with_empty_string(text):
        return text.replace('<Blank>', ' ')

    @staticmethod
    def get_values_as_a_list(values):
        new_values = values.split(',')
        list_values = []
        for new_val in new_values:
            list_values.append(new_val)
        return list_values

    @staticmethod
    def get_question_code_element(question_code):
        if len(question_code) > 4:
            return question_code.replace("Q", "")
        else:
            return question_code.replace("Q", "").zfill(4)
