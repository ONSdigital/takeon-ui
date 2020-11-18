class OverrideMessages:
    BMI_MESSAGES = {
        'fv override message': "Overridden - 'Invalid Value, please check'",
        'iv override message': "Overridden - 'This is not a valid brick type. "
                               "It should be 2 (clay), 3 (concrete) or 4 (sandlime)'",
        'popm override message': "Overridden - 'This has changed significantly since the last submission'",
        'popqvq override message': "Overridden - 'This has changed since last submission'",
        'popzc override message': "Overridden - 'This is different to the previous submission. "
                                  "If this is 0 or blank, the previous was greater. "
                                  "If this has a value, the previous was 0 or blank'",
        'qvq override message': "Overridden - 'This total is not equal to the derived total'",
        'qvv override message': "Overridden - 'There is a comment from this contributor'"
    }

    RSI_MESSAGES = {
        'poprrm override message': "Overridden - 'Internet turnover to total turnover ratio - "
                                   "large month on month change'",
        'ppvb total turnover override message': "Overridden - "
                                                "'Total turnover(Q20) was returned blank in the previous period'",
        'ppvb internet sales override message': "Overridden - "
                                                "'Internet Sales(Q21) was returned blank in the previous period'",
        'qvv override message': "Overridden - 'Respondent entered a comment'",
        'vb override message': "Overridden - 'Total turnover(Q20) is blank'",
        'vz override message': "Overridden - 'Total turnover(Q20) is zero'",
        'vpsic override message': "Overridden - 'SIC is petrol and internet sales(Q21) value is greater than zero'"
    }

    TEST_SURVEY_MESSAGES = {
        'qvv override message': "Overridden - 'There is a comment from this contributor'"
    }

    @staticmethod
    def get_expected_override_message(survey, message):
        if survey == '023':
            messages = OverrideMessages.RSI_MESSAGES
        elif survey == '999A':
            messages = OverrideMessages.TEST_SURVEY_MESSAGES
        else:
            messages = OverrideMessages.BMI_MESSAGES
        if message.lower() in messages:
            return messages.get(message)
        else:
            assert False, 'No, key with the name: "' + message + '" does not exists in dictionary'
