# Function to group data by question code across periods in order for it to print on to HTML layout properly
# and to only pick up questions from current period's form

def group_historic_data(historic_data):
    try:
        questions_dictionary = {}
        historic_questions = historic_data['history_data'][0]['view_form_responses']
        historic_questions_list = gather_historic_questions(historic_questions)
        for question in historic_questions_list:
            question_responses = []
            for row in historic_data['history_data']:
                for response in row['view_form_responses']:
                    if question == response['questioncode']:
                        question_responses.append(response['response'])
            questions_dictionary[question] = question_responses
    except IndexError as Error:
        print("No historic forms: " + str(Error))
        return questions_dictionary

    return questions_dictionary


def gather_historic_questions(historic_questions):
    historic_questions_list = []
    for row in historic_questions:
        if row['type'] == 'NUMERIC':
            historic_questions_list.append(row['questioncode'])
    return historic_questions_list
