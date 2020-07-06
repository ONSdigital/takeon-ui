class ReportingHelper:

    @staticmethod
    def check_single_message_matches(question, act_msg, exp_msg):
        if act_msg == exp_msg:
            return True
        else:
            assert False, 'Expected message is "' + exp_msg + '" but the Actual message was "' + act_msg + '" for question ' + question

    @staticmethod
    def check_single_message_not_matches(question, act_msg, exp_msg):
        if act_msg != exp_msg:
            return True
        else:
            assert False, 'This message "' + act_msg + '" is not expected for question ' + question

    @staticmethod
    def check_multiple_messages_matches(question, act_msgs, exp_msg):
        is_validation = False
        for act_msg in act_msgs:
            if act_msg.text == exp_msg:
                is_validation = True
        if not is_validation:
            assert False, 'Expected message is "' + exp_msg + '" but the Actual message was "' + act_msgs + '" for question ' + question

    @staticmethod
    def check_multiple_messages_not_matches(question, act_msg, exp_msg):
        exp_msgs = (exp_msg.split(','))
        is_validation = False
        for exp_mg in exp_msgs:
            if act_msg != exp_mg:
                is_validation = True
        if not is_validation:
            assert False, 'This message "' + act_msg + '" is not expected for question ' + question

    @staticmethod
    def compare_the_messages(operator_type, act_msg, exp_msg, result):
        if operator_type == 'greater than':
            ReportingHelper.check_greater_than(act_msg, exp_msg)
            ReportingHelper.check_single_message_matches('', result, 'true')
        elif operator_type == 'less than':
            ReportingHelper.check_less_than(act_msg, exp_msg)
            ReportingHelper.check_single_message_matches('', result, 'false')
        elif operator_type == 'equal to':
            ReportingHelper.check_single_message_matches('', act_msg, exp_msg)
            ReportingHelper.check_single_message_matches('', result, 'false')

    @staticmethod
    def check_greater_than(act_msg, exp_msg):
        if act_msg > exp_msg:
            return True
        else:
            assert False, 'Expected value "' + exp_msg + '" is not greater than "' + act_msg

    @staticmethod
    def compare_the_values(operator_type, value_one, value_two):
        if operator_type == 'greater than' and value_one > value_two:
            return True
        elif operator_type == 'less than' and value_one < value_two:
            return False
        elif operator_type == 'equal to' and value_one == value_two:
            return True

    @staticmethod
    def check_less_than(act_msg, exp_msg):
        if act_msg < exp_msg:
            return True
        else:
            assert False, 'Expected value "' + exp_msg + '" is not less than "' + act_msg
