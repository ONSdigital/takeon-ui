class ValidationMessages:
    BMI_MESSAGES = {
        'invalid value validation': 'This is not a valid brick type. It should be 2 (clay), 3 (concrete) or 4 (sandlime)'
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

    @staticmethod
    def get_validation_message(survey, message):
        if survey == '023':
            messages = ValidationMessages.RSI_MESSAGES
        elif survey == '999A':
            messages = ''
        else:
            messages = ValidationMessages.BMI_MESSAGES
        if message.lower() in messages:
            return messages.get(message)
        else:
            assert False, message + ' validation message type from the scenario does not exists'
