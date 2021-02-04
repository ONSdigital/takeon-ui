# import pytest
# from app.utilities.parse_historic_data import group_historic_data, gather_historic_questions

# historic_data = {
# 		'history_data': [{
# 				'reference': '12345678011',
# 				'period': '201801',
# 				'view_form_responses': [{
# 					'displaytext': 'This is a numeric question - Total turnover',
# 					'instance': 0,
# 					'response': '5',
# 					'questioncode': '1000',
# 					'displayorder': 1,
# 					'displayquestionnumber': 'Q1',
# 					'type': 'NUMERIC'
# 				}, {
# 					'displaytext': 'This is another numeric question - Internet Sales',
# 					'instance': 0,
# 					'response': '6',
# 					'questioncode': '1001',
# 					'displayorder': 2,
# 					'displayquestionnumber': 'Q2',
# 					'type': 'NUMERIC'
# 				}],
# 			'survey': '999A'
# 		},
# 		{
# 			'reference': '12345678011',
# 			'period': '201712',
# 			'view_form_responses': [{
# 				'displaytext': 'This is a numeric question - Total turnover',
# 				'instance': 0,
# 				'response': '4',
# 				'questioncode': '1000',
# 				'displayorder': 1,
# 				'displayquestionnumber': 'Q1',
# 				'type': 'NUMERIC'
# 			}, {
# 				'displaytext': 'This is another numeric question - Internet Sales',
# 				'instance': 0,
# 				'response': '5',
# 				'questioncode': '1001',
# 				'displayorder': 2,
# 				'displayquestionnumber': 'Q2',
# 				'type': 'NUMERIC'
# 			}],
#             'survey': '999A'
# 		}]}

# historic_questions = [{
#             'displaytext': 'This is a numeric question - Total turnover',
#             'instance': 0,
#             'response': '5',
#             'questioncode': '1000',
#             'displayorder': 1,
#             'displayquestionnumber': 'Q1',
#             'type': 'NUMERIC'
#         }, {
#             'displaytext': 'This is another numeric question - Internet Sales',
#             'instance': 0,
#             'response': '6',
#             'questioncode': '1001',
#             'displayorder': 2,
#             'displayquestionnumber': 'Q2',
#             'type': 'NUMERIC'
#         }]

# def test_parse_historic_data_returns_grouped_output():
#     expected_output = {'1000': ['5', '4'], '1001': ['6', '5']}
#     assert group_historic_data(historic_data) == expected_output

# def test_gather_historic_questions_returns_expected_questions():
#     expected_output = ['1000', '1001']
#     assert gather_historic_questions(historic_questions) == expected_output

# def test_empty_array_returns_empty_dictionary():
#     empty_historic_data = {'history_data': []}
#     expected_output = {}
#     assert group_historic_data(empty_historic_data) == expected_output