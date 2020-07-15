import pytest
from app.utilities.helpers import question_order


data_output = {'form_validation_outputs': [{'questioncode': '1000', 'response': '', 'displayquestionnumber': 'Q1', 'displaytext': 'This is a numeric question - Total turnover', 'displayorder': 20, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '1001', 'response': '', 'displayquestionnumber': 'Q2', 'displaytext': 'This is another numeric question - Internet Sales', 'displayorder': 2, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '2000', 'response': '', 'displayquestionnumber': 'Q3', 'displaytext': 'This is a checkbox question', 'displayorder': 3, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '3000', 'response': '', 'displayquestionnumber': 'Q4', 'displaytext': 'This is a text question', 'displayorder': 4, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '4000', 'response': '', 'displayquestionnumber': 'Q5', 'displaytext': 'This is a postive derived question', 'displayorder': 5, 'validation_info': [], 'panel': ''},
        {'questioncode': '4001', 'response': '', 'displayquestionnumber': 'Q6', 'displaytext': 'This is a subtracted derived question', 'displayorder': 6, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '5000', 'response': '', 'displayquestionnumber': 'Q7', 'displaytext': 'Comment Question (!= Blank)', 'displayorder': 7, 'validation_info': [], 'panel': ''},
        {'questioncode': '5001', 'response': '', 'displayquestionnumber': 'Q8', 'displaytext': 'Comment Question (= 2)', 'displayorder': 8, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '6000', 'response': '', 'displayquestionnumber': 'Q9', 'displaytext': 'Value is Blank Question (== Blank)', 'displayorder': 9, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '7000', 'response': '', 'displayquestionnumber': 'Q10', 'displaytext': 'Value is Zero question', 'displayorder': 10, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8000', 'response': '', 'displayquestionnumber': 'Q11', 'displaytext': 'Question vs Question (Total turnover)', 'displayorder': 11, 'validation_info': [], 'panel': ''},
        {'questioncode': '8001', 'response': '', 'displayquestionnumber': 'Q12', 'displaytext': 'Question vs Question (Internet sales)', 'displayorder': 12, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8100', 'response': '', 'displayquestionnumber': 'Q15', 'displaytext': 'Internet Sales (POPRRM validation)', 'displayorder': 13, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8101', 'response': '', 'displayquestionnumber': 'Q16', 'displaytext': 'Total turnover (POPRRM validation)', 'displayorder': 14, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '9000', 'response': '', 'displayquestionnumber': 'Q13', 'displaytext': 'VPSIC question', 'displayorder': 15, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '9001', 'response': '', 'displayquestionnumber': 'Q14', 'displaytext': 'Previous Period Value is Blank Question (Internet sales PP = Blank)', 'displayorder': 16, 'validation_info': [], 'panel': ''}]}

data_missing_key = {'form_validation_outputs': [{'questioncode': '1000', 'response': '', 'displayquestionnumber': 'Q1', 'displaytext': 'This is a numeric question - Total turnover', 'displayorder': 20, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '1001', 'response': '', 'displayquestionnumber': 'Q2', 'displaytext': 'This is another numeric question - Internet Sales', 'displayorder': 2, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '2000', 'response': '', 'displayquestionnumber': 'Q3', 'displaytext': 'This is a checkbox question', 'validation_info': [], 'panel': ''}, 
        {'questioncode': '3000', 'response': '', 'displayquestionnumber': 'Q4', 'displaytext': 'This is a text question', 'displayorder': 4, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '4000', 'response': '', 'displayquestionnumber': 'Q5', 'displaytext': 'This is a postive derived question', 'displayorder': 5, 'validation_info': [], 'panel': ''},
        {'questioncode': '4001', 'response': '', 'displayquestionnumber': 'Q6', 'displaytext': 'This is a subtracted derived question', 'displayorder': 6, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '5000', 'response': '', 'displayquestionnumber': 'Q7', 'displaytext': 'Comment Question (!= Blank)', 'displayorder': 7, 'validation_info': [], 'panel': ''},
        {'questioncode': '5001', 'response': '', 'displayquestionnumber': 'Q8', 'displaytext': 'Comment Question (= 2)', 'displayorder': 8, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '6000', 'response': '', 'displayquestionnumber': 'Q9', 'displaytext': 'Value is Blank Question (== Blank)', 'displayorder': 9, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '7000', 'response': '', 'displayquestionnumber': 'Q10', 'displaytext': 'Value is Zero question', 'displayorder': 10, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8000', 'response': '', 'displayquestionnumber': 'Q11', 'displaytext': 'Question vs Question (Total turnover)', 'displayorder': 11, 'validation_info': [], 'panel': ''},
        {'questioncode': '8001', 'response': '', 'displayquestionnumber': 'Q12', 'displaytext': 'Question vs Question (Internet sales)', 'displayorder': 12, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8100', 'response': '', 'displayquestionnumber': 'Q15', 'displaytext': 'Internet Sales (POPRRM validation)', 'displayorder': 13, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8101', 'response': '', 'displayquestionnumber': 'Q16', 'displaytext': 'Total turnover (POPRRM validation)', 'displayorder': 14, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '9000', 'response': '', 'displayquestionnumber': 'Q13', 'displaytext': 'VPSIC question', 'displayorder': 15, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '9001', 'response': '', 'displayquestionnumber': 'Q14', 'displaytext': 'Previous Period Value is Blank Question (Internet sales PP = Blank)', 'displayorder': 16, 'validation_info': [], 'panel': ''}]}

invalid_json = [{"invalid": "json"}]

empty_input_json = {}


def test_question_order_returns_expected_format():

    expected_output = {'form_validation_outputs': [{'questioncode': '1001', 'response': '', 'displayquestionnumber': 'Q2', 'displaytext': 'This is another numeric question - Internet Sales', 'displayorder': 2, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '2000', 'response': '', 'displayquestionnumber': 'Q3', 'displaytext': 'This is a checkbox question', 'displayorder': 3, 'validation_info': [], 'panel': ''}, {'questioncode': '3000', 'response': '', 'displayquestionnumber': 'Q4', 'displaytext': 'This is a text question', 'displayorder': 4, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '4000', 'response': '', 'displayquestionnumber': 'Q5', 'displaytext': 'This is a postive derived question', 'displayorder': 5, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '4001', 'response': '', 'displayquestionnumber': 'Q6', 'displaytext': 'This is a subtracted derived question', 'displayorder': 6, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '5000', 'response': '', 'displayquestionnumber': 'Q7', 'displaytext': 'Comment Question (!= Blank)', 'displayorder': 7, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '5001', 'response': '', 'displayquestionnumber': 'Q8', 'displaytext': 'Comment Question (= 2)', 'displayorder': 8, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '6000', 'response': '', 'displayquestionnumber': 'Q9', 'displaytext': 'Value is Blank Question (== Blank)', 'displayorder': 9, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '7000', 'response': '', 'displayquestionnumber': 'Q10', 'displaytext': 'Value is Zero question', 'displayorder': 10, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8000', 'response': '', 'displayquestionnumber': 'Q11', 'displaytext': 'Question vs Question (Total turnover)', 'displayorder': 11, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8001', 'response': '', 'displayquestionnumber': 'Q12', 'displaytext': 'Question vs Question (Internet sales)', 'displayorder': 12, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8100', 'response': '', 'displayquestionnumber': 'Q15', 'displaytext': 'Internet Sales (POPRRM validation)', 'displayorder': 13, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '8101', 'response': '', 'displayquestionnumber': 'Q16', 'displaytext': 'Total turnover (POPRRM validation)', 'displayorder': 14, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '9000', 'response': '', 'displayquestionnumber': 'Q13', 'displaytext': 'VPSIC question', 'displayorder': 15, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '9001', 'response': '', 'displayquestionnumber': 'Q14', 'displaytext': 'Previous Period Value is Blank Question (Internet sales PP = Blank)', 'displayorder': 16, 'validation_info': [], 'panel': ''}, 
        {'questioncode': '1000', 'response': '', 'displayquestionnumber': 'Q1', 'displaytext': 'This is a numeric question - Total turnover', 'displayorder': 20, 'validation_info': [], 'panel': ''}]}

    assert question_order(data_output) == expected_output


def test_missing_key_display_order():
    with pytest.raises(KeyError):
        question_order(data_missing_key)


def test_invalid_json_returns_type_error_json():
    with pytest.raises(TypeError):
        question_order(invalid_json)
        

def test_blank_json_returns_error_json():
    with pytest.raises(KeyError):
        question_order(empty_input_json)