class Utilities:

    @staticmethod
    def convert_blank_data_to_empty_string(data):
        if data.lower() == 'blank':
            data = ''
        return data
