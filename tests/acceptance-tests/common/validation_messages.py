class ValidationMessages:
    BMI_MESSAGES = {
        'fv validation': 'Value set to default, please check',
        'iv validation': 'This is not a valid brick type. It should be 2 (clay), 3 (concrete) or 4 (sandlime)',
        'popm validation': 'This has changed significantly since the last submission',
        'popqvq validation': 'This has changed since last submission',
        'popzc validation': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank',
        'qvq validation': 'This total is not equal to the derived total',
        'qvv validation': 'There is a comment from this contributor',

    }

    RSI_MESSAGES = {
        'popmrz validation': 'This value is 0. Previous period it was more than a certain percentage of the total.',
        'poprrm validation': 'The ratio of ratios between values has changed significantly since the last submission',
        'ppvb validation': 'This value was blank in the previous period',
        'qvq validation': 'This is greater than the question we compare it to',
        'qvqt validation': 'Total different to calculated total (allowing for margin)',
        'qvv validation': 'There is a comment from this contributor',
        'vb validation': 'This value is blank',
        'vz validation': 'This value is zero',
        'vb and vz validation': 'This value is zero,This value is blank',
        'vpsic validation': 'Check the response to this question'

    }

    TEST_SURVEY_MESSAGES = {
        'qvv validation': 'There is a comment from this contributor'
    }

    @staticmethod
    def get_expected_validation_message(survey, message):
        if survey == '023':
            messages = ValidationMessages.RSI_MESSAGES
        elif survey == '999A':
            messages = ValidationMessages.TEST_SURVEY_MESSAGES
        else:
            messages = ValidationMessages.BMI_MESSAGES
        if message.lower() in messages:
            return messages.get(message)
        else:
            assert False, message + ' validation message type from the scenario does not exists'
