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
    def get_question_code_element(question_code):
        if len(question_code) > 4:
            return question_code.replace("Q", "")
        else:
            return question_code.replace("Q", "").zfill(4)
