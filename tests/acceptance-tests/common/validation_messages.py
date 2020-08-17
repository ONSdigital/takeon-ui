class ValidationMessages:
    BMI_MESSAGES = {
        'fv validation': 'Value set to default, please check',
        'iv validation': 'This is not a valid brick type. It should be 2 (clay), 3 (concrete) or 4 (sandlime)',
        'popm validation': 'This has changed significantly since the last submission',
        'popqvq validation': 'This has changed since last submission',
        'popzc validation': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank',
        'qvq validation': 'This total is not equal to the derived total',
        'qvv validation': 'There is a comment from this contributor'
    }

    RSI_MESSAGES = {
        'popmrz validation': 'Internet value(Q21) = 0 this period but > 0 last period and ratio of Internet(Q21) to total turnover(Q20) was > 10% last period',
        'poprrm validation': 'Internet turnover to total turnover ratio - large month on month change',
        'ppvb total turnover validation': 'Total turnover(Q20) was returned blank in the previous period',
        'ppvb internet sales validation': 'Internet Sales(Q21) was returned blank in the previous period',
        'qvq validation': 'Internet turnover(Q21) is greater than total turnover(Q20)',
        'qvqt validation': 'Commodity total does not equal the total turnover (allowing for margin of 5)',
        'qvv validation': 'Respondent entered a comment',
        'vb validation': 'Total turnover(Q20) is blank',
        'vz validation': 'Total turnover(Q20) is zero',
        'vb and vz validation': 'Total turnover(Q20) is zero,Total turnover(Q20) is blank',
        'vpsic validation': 'SIC is petrol and internet sales(Q21) value is greater than zero'
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
