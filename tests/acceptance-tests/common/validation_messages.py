class ValidationMessages:
    BMI_MESSAGES = {
        'fv validation': 'Warning - Invalid Value, please check',
        'iv validation': 'Warning - This is not a valid brick type. It should be 2 (clay), 3 (concrete) or 4 (sandlime)',
        'popm validation': 'Warning - This has changed significantly since the last submission',
        'popqvq validation': 'Warning - This has changed since last submission',
        'popzc validation': 'Warning - This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank',
        'qvq validation': 'Warning - This total is not equal to the derived total',
        'qvv validation': 'Warning - There is a comment from this contributor'
    }

    RSI_MESSAGES = {
        'popmrz validation': 'Error - Internet value(Q21) = 0 this period but > 0 last period and ratio of Internet(Q21) to total turnover(Q20) was > 10% last period',
        'poprrm validation': 'Warning - Internet turnover to total turnover ratio - large month on month change',
        'ppvb total turnover validation': 'Warning - Total turnover(Q20) was returned blank in the previous period',
        'ppvb internet sales validation': 'Warning - Internet Sales(Q21) was returned blank in the previous period',
        'qvq validation': 'Error - Internet turnover(Q21) is greater than total turnover(Q20)',
        'qvqt validation': 'Error - Commodity total does not equal the total turnover (allowing for margin of 5)',
        'qvv validation': 'Warning - Respondent entered a comment',
        'vb validation': 'Warning - Total turnover(Q20) is blank',
        'vz validation': 'Warning - Total turnover(Q20) is zero',
        'vb and vz validation': 'Warning - Total turnover(Q20) is zero,Warning - Total turnover(Q20) is blank',
        'vpsic validation': 'Warning - SIC is petrol and internet sales(Q21) value is greater than zero'
    }

    TEST_SURVEY_MESSAGES = {
        'qvv validation': 'Warning - There is a comment from this contributor',
        'qvv text validation': 'Warning - Respondent entered a comment',
        'fv validation': 'Warning - Value set to default, please check',
        'vz validation': 'Warning - This value is Zero',
        'vb validation': 'Warning - This value is blank',
        'vn validation': 'Warning - This is a negative value',
        'vp validation': 'Warning - Respondent entered a value',
        'vi validation': 'Warning - Brick type is invalid',
        'vpsic validation': 'Warning - SIC is petrol and value is greater than zero',
        'qvqt validation': 'Error - Derived total does not equal the total (allowing for margin of 5)',
        'qvq validation': 'Error - This is greater than the comparison question',
        'qvdq validation': 'Warning - This total is not equal to the derived total',
        'popmrz validation': 'Error - This value is 0. Previous period it was more than a certain percentage of the total'
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
            assert False, 'No, key with the name: "' + message + '" does not exists in dictionary'
