# Combine Response and Validation data for new UI Layout
# from app.utilities.helpers import json_validator

def combine_response_validations(view_form_data, validations):
    try:
        combined_array = []
        for contributor in view_form_data['view_form_responses']:
            overridden_count = 0
            combined_output = {}
            validation_info_array = []
            qcode = contributor['questioncode']
            response = contributor['response']
            adjusted_response = contributor['adjustedresponse']
            combined_output['questioncode'] = qcode
            combined_output['response'] = response
            combined_output['adjustedresponse'] = adjusted_response
            combined_output['displayquestionnumber'] = contributor['displayquestionnumber']
            combined_output['displaytext'] = contributor['displaytext']
            combined_output['displayorder'] = contributor['displayorder']
            combined_output['type'] = contributor['type']
            for validation in validations['validation_outputs']:
                validation_failure = {}
                if validation['primaryquestion'] == qcode:
                    validation_failure['name'] = validation['name']
                    validation_failure['overridden'] = validation['overridden']
                    validation_failure['validationoutputid'] = validation['validationoutputid']
                    validation_failure['triggered'] = validation['triggered']
                    validation_failure['validationmessage'] = validation['validationmessage']
                    if validation['overridden']:
                        overridden_count += 1
                    validation_info_array.append(validation_failure)
                if overridden_count == len(validation_info_array):
                    combined_output['panel'] = 'panel--info'
                else:
                    combined_output['panel'] = 'panel--error'
            combined_output['validation_info'] = validation_info_array
            combined_array.append(combined_output)

        combined_dictionary_output = {}
        combined_dictionary_output['form_validation_outputs'] = combined_array

    except ValueError as value_error:
        print("Error with JSON Structure: " + str(value_error))
        raise ValueError
    except KeyError as key_error:
        print("Error with missing JSON Keys " + str(key_error))
        raise KeyError
    except TypeError as type_error:
        print("Error with data type converting to JSON " + str(type_error))
        raise TypeError

    return combined_dictionary_output
