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
