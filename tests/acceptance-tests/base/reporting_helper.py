class ReportingHelper:

    @staticmethod
    def check_values_matches(question,value_one, value_two):
        if value_one == value_two:
            return True
        else:
            assert False, '"' + value_one + '" did not matched with "' + value_two + '" for question ' + question

    @staticmethod
    def check_values_not_matches(value_one, value_two):
        if value_one != value_two:
            return True
        else:
            assert False, '"' + value_one + '" matched with "' + value_two + '"'
