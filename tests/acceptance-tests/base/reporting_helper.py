class ReportingHelper:

    @staticmethod
    def check_single_message_matches(question, act_msg, exp_msg):
        if act_msg == exp_msg:
            return True
        else:
            assert False, 'Expected message is "' + exp_msg + '" but the Actual message was "' + act_msg + '" for question ' + question

    @staticmethod
    def check_single_message_not_matches(act_msg, exp_msg, question=None, message=None):
        if act_msg != exp_msg:
            return True
        elif act_msg == exp_msg and not question:
            assert False, message + 'The validation status should not be "' + act_msg + '"'
        else:
            assert False, 'This message "' + act_msg + '" is not expected for question ' + question

    @staticmethod
    def check_elements_message_matches(question, elements, exp_msg):
        if len(elements) != 0:
            is_validation = False
            msgs = []
            for element in elements:
                if element.text == exp_msg:
                    is_validation = True
                else:
                    msgs.append(element.text)
            if not is_validation:
                assert False, 'Expected message is "' + exp_msg + '" did not exists in messages list"\n' + '\n'.join(
                    msgs) + '" for question ' + question
        else:
            assert False, 'Expected message is "' + exp_msg + '" but the Actual message elements returned "' + str(
                len(elements)) + '".Please check the element locator for question ' + question

    @staticmethod
    def check_messages_matches(question, act_msgs, exp_msg):
        if len(act_msgs) != 0:
            is_validation = False
            msgs = []
            for act_msg in act_msgs:
                if act_msg == exp_msg:
                    is_validation = True
                else:
                    msgs.append(act_msg)
            if not is_validation:
                assert False, 'Expected message is "' + exp_msg + '" did not exists in messages list"\n' + '\n'.join(
                    msgs) + '" for question ' + question
        else:
            assert False, 'Expected message is "' + exp_msg + '" but the Actual message elements returned "' + str(
                len(act_msgs)) + '".Please check the element locator for question ' + question

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
    def compare_values(value_one, value_two):
        if int(value_one) != int(value_two):
            return True
        else:
            assert False, 'Expected value "' + str(value_one) + '" should not be equal to actual value"' + str(
                value_two) + '"'

    @staticmethod
    def compare_values_are_not_equal(value_one, value_two):
        if int(value_one) != int(value_two):
            return True
        else:
            return False

    @staticmethod
    def compare_the_zero_movement_values(value_one, value_two):
        if int(value_one) == 0 and int(value_two) > 0:
            return True
        elif int(value_one) > 0 and int(value_two) == 0:
            return True
        else:
            return False

    @staticmethod
    def compare_strings(actual_msg, exp_msg):
        if actual_msg != exp_msg:
            return True
        else:
            return False

    @staticmethod
    def check_greater_than(act_msg, exp_msg):
        if act_msg > exp_msg:
            return True
        else:
            assert False, 'Expected value "' + exp_msg + '" is not greater than "' + act_msg

    @staticmethod
    def compare_the_values_with_operator(operator_type, value_one, value_two):
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
