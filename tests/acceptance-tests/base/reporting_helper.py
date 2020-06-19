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

    @staticmethod
    def compare_the_values(operator_type, act_msg, exp_msg, result):
        if operator_type == 'greater than':
            ReportingHelper.check_greater_than(act_msg, exp_msg)
            ReportingHelper.check_values_matches('', result, 'true')
        elif operator_type == 'less than':
            ReportingHelper.check_less_than(act_msg, exp_msg)
            ReportingHelper.check_values_matches('', result, 'false')
        elif operator_type == 'equal to':
            ReportingHelper.check_values_matches('', act_msg, exp_msg)
            ReportingHelper.check_values_matches('', result, 'false')

    @staticmethod
    def check_greater_than(act_msg, exp_msg):
        if act_msg > exp_msg:
            return True
        else:
            assert False, 'Expected value "' + exp_msg + '" is not greater than "' + act_msg

    @staticmethod
    def check_less_than(act_msg, exp_msg):
        if act_msg < exp_msg:
            return True
        else:
            assert False, 'Expected value "' + exp_msg + '" is not less than "' + act_msg
