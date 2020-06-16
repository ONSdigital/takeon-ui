class ReportingHelper:

    @staticmethod
    def check_values_matches(question, value_one, value_two):
        if value_one == value_two:
            return True
        else:
            assert False, '"' + value_one + '" did not match with "' + value_two + '" for question ' + question

    @staticmethod
    def check_values_not_matches(question, value_one, value_two):
        if value_one != value_two:
            return True
        else:
            assert False, '"' + value_one + '" matches with "' + value_two + '" for question ' + question
