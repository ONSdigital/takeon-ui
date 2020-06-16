class ReportingHelper:

    @staticmethod
    def check_values_matches(question, act_msg, exp_msg):
        if act_msg == exp_msg:
            return True
        else:
            assert False, 'Expected message is "' + exp_msg + '" but the Actual message was "' + act_msg + '" for question ' + question

    @staticmethod
    def check_values_not_matches(question, act_msg, exp_msg):
        if act_msg != exp_msg:
            return True
        else:
            assert False, 'This message "' + act_msg + '" is not expected for question ' + question
