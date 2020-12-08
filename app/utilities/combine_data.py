# Combine Form response and Validation data

def extract_question_data(form_data, index):
    question_data = {}
    qcode = form_data['view_form_responses'][index]['questioncode']
    response = form_data['view_form_responses'][index]['response']
    adjusted_response = form_data['view_form_responses'][index]['adjustedresponse']
    question_data['questioncode'] = qcode
    question_data['response'] = response
    question_data['adjustedresponse'] = adjusted_response
    question_data['displayquestionnumber'] = form_data['view_form_responses'][index]['displayquestionnumber']
    question_data['displaytext'] = form_data['view_form_responses'][index]['displaytext']
    question_data['displayorder'] = form_data['view_form_responses'][index]['displayorder']
    question_data['type'] = form_data['view_form_responses'][index]['type']
    return question_data


def extract_validation_data(extracted_form_data, validation_data):
    validation_info_array = []
    overridden_count = 0
    panel = ''
    for validation in validation_data['validation_outputs']:
        validation_failure = {}
        if validation['primaryquestion'] == extracted_form_data['questioncode']:
            validation_failure['name'] = validation['name']
            validation_failure['overridden'] = validation['overridden']
            validation_failure['validationoutputid'] = validation['validationoutputid']
            validation_failure['triggered'] = validation['triggered']
            validation_failure['validationmessage'] = validation['validationmessage']
            validation_failure['description'] = validation['description']
            validation_failure['severity'] = validation['severity']
            if validation['overridden']:
                overridden_count += 1
            validation_info_array.append(validation_failure)
        panel = decide_panel_colour(overridden_count, validation_info_array)
    return validation_info_array, panel


def decide_panel_colour(overridden_count, validation_info_array):
    if overridden_count == len(validation_info_array):
        panel = 'panel--info'
    else:
        panel = 'panel--error'
    return panel


def combine_responses_and_validations(form_data, validation_data):
    try:
        counter = 0
        combined_array = []
        while counter < len(form_data['view_form_responses']):
            temp_question_data = extract_question_data(form_data, counter)
            output = extract_validation_data(temp_question_data, validation_data)
            temp_question_data['validation_info'] = output[0]
            temp_question_data['panel'] = output[1]
            combined_array.append(temp_question_data)
            counter += 1
        output_dictionary = {}
        output_dictionary['form_validation_outputs'] = combined_array
        return output_dictionary
    except ValueError as value_error:
        print("Error with JSON Structure: " + str(value_error))
        raise ValueError
    except KeyError as key_error:
        print("Error with missing JSON Keys " + str(key_error))
        raise KeyError
    except TypeError as type_error:
        print("Error with data type converting to JSON " + str(type_error))
        raise TypeError
