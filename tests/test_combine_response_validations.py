import pytest
from app.utilities.combine_data import combine_responses_and_validations


form_output = {'view_form_responses': [{'displaytext': 'Comment on the figures included in your return', 'displayorder': '11', 'instance': 0,'response': '1', 'questioncode': '0146', 'displayquestionnumber': 'Q146', 'type': 'NUMERIC'},
{'displaytext': 'New pits or quarries brought into use since date of last return', 'displayorder': '10', 'instance': 0, 'response': '2', 'questioncode': '0147', 'displayquestionnumber': 'Q147', 'type': 'NUMERIC'},
{'displaytext': 'Sand produced for asphalt (asphalting sand)', 'displayorder': '1','instance': 0, 'response': '2342345', 'questioncode': '0601', 'displayquestionnumber': 'Q601', 'type': 'NUMERIC'},
{'displaytext': 'Sand produced for use in mortar (building or soft sand)', 'displayorder': '2', 'instance': 0, 'response': '20000', 'questioncode': '0602', 'displayquestionnumber': 'Q602', 'type': 'NUMERIC'},
{'displaytext': 'Sand produced for concreting (sharp sand)', 'displayorder': '3', 'instance': 0, 'response': '5', 'questioncode': '0603', 'displayquestionnumber': 'Q603', 'type': 'NUMERIC'},
{'displaytext': 'Gravel coated with bituminous binder (on or off site)', 'displayorder': '4', 'instance': 0, 'response': '6', 'questioncode': '0604', 'displayquestionnumber': 'Q604', 'type': 'NUMERIC'},
{'displaytext': 'Gravel produced for concrete aggregate (including sand/gravel mixes)', 'displayorder': '5', 'instance': 0, 'response': '7', 'questioncode': '0605', 'displayquestionnumber': 'Q605', 'type': 'NUMERIC'},
{'displaytext': 'Other screened and graded gravels', 'displayorder': '6', 'instance': 0, 'response': '8', 'questioncode': '0606', 'displayquestionnumber': 'Q606', 'type': 'NUMERIC'},
{'displaytext': 'Sand and gravel used for constructional fill', 'displayorder': '7', 'instance': 0, 'response': '15', 'questioncode': '0607', 'displayquestionnumber': 'Q607', 'type': 'NUMERIC'},
{'displaytext': 'TOTALS', 'displayorder': '8', 'instance': 0, 'response': '102', 'questioncode': '0608', 'displayquestionnumber': 'Q608', 'type': 'NUMERIC'},
{'displaytext': 'Derived Total of all sand and gravel (Q601 + Q602 + Q603 + Q604 + Q605 + Q606 + Q607)', 'displayorder': '9', 'instance': 0, 'response': '2362386', 'questioncode': '9001', 'displayquestionnumber': 'Q9001', 'type': 'NUMERIC'}]}

validation_output = {'validation_outputs': [{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6620, 'rule': 'POPZC', 'overridden': False, 'primaryquestion': '0601', 'validationoutputid': 2758, 'lastupdateddate': '2020-02-28T10:08:59.638+00:00', 'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity', 'formula': '2342345 != 0 AND ( 2342345 = 0 OR 0 = 0 ) AND abs(2342345 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6621, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0602', 'validationoutputid': 2759, 'lastupdateddate': '2020-02-27T16:30:29.166+00:00', 'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity', 'formula': '20000 != 0 AND ( 20000 = 0 OR 0 = 0 ) AND abs(20000 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6622, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0603', 'validationoutputid': 2760, 'lastupdateddate': '2020-02-26T16:52:27.388+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '5 != 0 AND ( 5 = 0 OR 0 = 0 ) AND abs(5 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6623, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0604', 'validationoutputid': 2761, 'lastupdateddate': '2020-02-26T16:49:47.758+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '6 != 0 AND ( 6 = 0 OR 0 = 0 ) AND abs(6 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6624, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0605', 'validationoutputid': 2762, 'lastupdateddate': '2020-02-26T15:30:44.576+00:00', 'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity', 'formula': '7 != 0 AND ( 7 = 0 OR 0 = 0 ) AND abs(7 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6625, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0606', 'validationoutputid': 2763, 'lastupdateddate': '2020-02-27T15:18:02.421+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '8 != 0 AND ( 8 = 0 OR 0 = 0 ) AND abs(8 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6626, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0607', 'validationoutputid': 2764, 'lastupdateddate': '2020-02-27T15:18:02.421+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '15 != 0 AND ( 15 = 0 OR 0 = 0 ) AND abs(15 - 0) > 0', 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6640, 'rule': 'CPBMI', 'overridden': True, 'primaryquestion': '0147', 'validationoutputid': 2766, 'lastupdateddate': '2020-02-27T16:28:42.497+00:00', 'lastupdatedby': '', 'name': 'Comment Present (BMI)', 'formula': '2 = 2', 'validationmessage': 'Respondent entered a comment'}, {'severity': 'W', 'triggered': True, 'instance': '0', 'validationid': 6650, 'rule': 'QVDQ', 'overridden': False, 'primaryquestion': '0608', 'validationoutputid': 2767, 'lastupdateddate': '2020-02-28T10:08:59.638+00:00', 'lastupdatedby': 'fisdba', 'name': 'Question vs Derived Question', 'formula': '102 != 2362386', 'validationmessage': 'This total is not equal to the derived total'}]}

invalid_validation_output = {'validation_outputs': [{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6620, 'rule': 'POPZC', 'overridden': False, 'primaryquestion': '0601', 'validationoutputid': 2758, 'lastupdateddate': '2020-02-28T10:08:59.638+00:00', 'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity', 'formula': '2342345 != 0 AND ( 2342345 = 0 OR 0 = 0 ) AND abs(2342345 - 0) > 0'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6621, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0602', 'validationoutputid': 2759, 'lastupdateddate': '2020-02-27T16:30:29.166+00:00', 'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity', 'formula': '20000 != 0 AND ( 20000 = 0 OR 0 = 0 ) AND abs(20000 - 0) > 0'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6622, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0603', 'validationoutputid': 2760, 'lastupdateddate': '2020-02-26T16:52:27.388+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '5 != 0 AND ( 5 = 0 OR 0 = 0 ) AND abs(5 - 0) > 0'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6623, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0604', 'validationoutputid': 2761, 'lastupdateddate': '2020-02-26T16:49:47.758+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '6 != 0 AND ( 6 = 0 OR 0 = 0 ) AND abs(6 - 0) > 0'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6624, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0605', 'validationoutputid': 2762, 'lastupdateddate': '2020-02-26T15:30:44.576+00:00', 'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity', 'formula': '7 != 0 AND ( 7 = 0 OR 0 = 0 ) AND abs(7 - 0) > 0'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6625, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0606', 'validationoutputid': 2763, 'lastupdateddate': '2020-02-27T15:18:02.421+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '8 != 0 AND ( 8 = 0 OR 0 = 0 ) AND abs(8 - 0) > 0', },
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6626, 'rule': 'POPZC', 'overridden': True, 'primaryquestion': '0607', 'validationoutputid': 2764, 'lastupdateddate': '2020-02-27T15:18:02.421+00:00', 'lastupdatedby': '', 'name': 'Period on Period Zero Continuity', 'formula': '15 != 0 AND ( 15 = 0 OR 0 = 0 ) AND abs(15 - 0) > 0'},
{'severity': 'E', 'triggered': True, 'instance': '0', 'validationid': 6640, 'rule': 'CPBMI', 'overridden': True, 'primaryquestion': '0147', 'validationoutputid': 2766, 'lastupdateddate': '2020-02-27T16:28:42.497+00:00', 'lastupdatedby': '', 'name': 'Comment Present (BMI)', 'formula': '2 = 2', 'validationmessage': 'Respondent entered a comment'}, {'severity': 'W', 'triggered': True, 'instance': '0', 'validationid': 6650, 'rule': 'QVDQ', 'overridden': False, 'primaryquestion': '0608', 'validationoutputid': 2767, 'lastupdateddate': '2020-02-28T10:08:59.638+00:00', 'lastupdatedby': 'fisdba', 'name': 'Question vs Derived Question', 'formula': '102 != 2362386'}]}

blank_form_output = {'view_form_responses': [{'displaytext': 'Comment on the figures included in your return', 'displayorder': '11', 'instance': '', 'response': '', 'questioncode': '0146', 'displayquestionnumber': 'Q146', 'type': 'NUMERIC'},
{'displaytext': 'New pits or quarries brought into use since date of last return', 'displayorder': '10', 'instance': '', 'response': '', 'questioncode': '0147', 'displayquestionnumber': 'Q147', 'type': 'NUMERIC'},
{'displaytext': 'Sand produced for asphalt (asphalting sand)', 'displayorder': '1', 'instance': '', 'response': '', 'questioncode': '0601', 'displayquestionnumber': 'Q601', 'type': 'NUMERIC'},
{'displaytext': 'Sand produced for use in mortar (building or soft sand)', 'displayorder': '2', 'instance': '', 'response': '', 'questioncode': '0602', 'displayquestionnumber': 'Q602', 'type': 'NUMERIC'},
{'displaytext': 'Sand produced for concreting (sharp sand)', 'displayorder': '3', 'instance': '', 'response': '', 'questioncode': '0603', 'displayquestionnumber': 'Q603', 'type': 'NUMERIC'},
{'displaytext': 'Gravel coated with bituminous binder (on or off site)', 'displayorder': '4', 'instance': '', 'response': '', 'questioncode': '0604', 'displayquestionnumber': 'Q604', 'type': 'NUMERIC'},
{'displaytext': 'Gravel produced for concrete aggregate (including sand/gravel mixes)', 'displayorder': '5', 'instance': '', 'response': '', 'questioncode': '0605', 'displayquestionnumber': 'Q605', 'type': 'NUMERIC'},
{'displaytext': 'Other screened and graded gravels', 'displayorder': '6', 'instance': '', 'response': '', 'questioncode': '0606', 'displayquestionnumber': 'Q606', 'type': 'NUMERIC'},
{'displaytext': 'Sand and gravel used for constructional fill', 'displayorder': '7', 'instance': '', 'response': '', 'questioncode': '0607', 'displayquestionnumber': 'Q607', 'type': 'NUMERIC'},
{'displaytext': 'TOTALS', 'displayorder': '8', 'instance': '', 'response': '', 'questioncode': '0608', 'displayquestionnumber': 'Q608', 'type': 'NUMERIC'},
{'displaytext': 'Derived Total of all sand and gravel (Q601 + Q602 + Q603 + Q604 + Q605 + Q606 + Q607)', 'displayorder': '9', 'instance': '', 'response': '', 'questioncode': '9001', 'displayquestionnumber': 'Q9001', 'type': 'NUMERIC'}]}

blank_validations_output = {'validation_outputs': []}

invalid_json = [{"invalid": "json"}]

empty_input_json = {}

def test_combine_data_returns_expected_format():
    expected_output = {'form_validation_outputs': [{'questioncode': '0146', 'response': '1', 'displayquestionnumber': 'Q146', 'displaytext': 'Comment on the figures included in your return', 'displayorder': '11', 'validation_info': [], 'panel': 'panel--info'},
    {'questioncode': '0147', 'response': '2', 'displayquestionnumber': 'Q147', 'displaytext': 'New pits or quarries brought into use since date of last return', 'displayorder': '10', 'validation_info': [{'name': 'Comment Present (BMI)', 'overridden': True, 'validationoutputid': 2766, 'triggered': True, 'validationmessage': 'Respondent entered a comment'}], 'panel': 'panel--info'},
    {'questioncode': '0601', 'response': '2342345', 'displayquestionnumber': 'Q601', 'displaytext': 'Sand produced for asphalt (asphalting sand)', 'displayorder': '1', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': False, 'validationoutputid': 2758, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--error'},
    {'questioncode': '0602', 'response': '20000', 'displayquestionnumber': 'Q602', 'displaytext': 'Sand produced for use in mortar (building or soft sand)', 'displayorder': '2', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': True, 'validationoutputid': 2759, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--info'},
    {'questioncode': '0603', 'response': '5', 'displayquestionnumber': 'Q603', 'displaytext': 'Sand produced for concreting (sharp sand)', 'displayorder': '3', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': True, 'validationoutputid': 2760, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--info'},
    {'questioncode': '0604', 'response': '6', 'displayquestionnumber': 'Q604', 'displaytext': 'Gravel coated with bituminous binder (on or off site)', 'displayorder': '4', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': True, 'validationoutputid': 2761, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--info'},
    {'questioncode': '0605', 'response': '7', 'displayquestionnumber': 'Q605', 'displaytext': 'Gravel produced for concrete aggregate (including sand/gravel mixes)', 'displayorder': '5', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': True, 'validationoutputid': 2762, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--info'},
    {'questioncode': '0606', 'response': '8', 'displayquestionnumber': 'Q606', 'displaytext': 'Other screened and graded gravels', 'displayorder': '6', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': True, 'validationoutputid': 2763, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--info'},
    {'questioncode': '0607', 'response': '15', 'displayquestionnumber': 'Q607', 'displaytext': 'Sand and gravel used for constructional fill', 'displayorder': '7', 'validation_info': [{'name': 'Period on Period Zero Continuity', 'overridden': True, 'validationoutputid': 2764, 'triggered': True, 'validationmessage': 'This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank'}], 'panel': 'panel--info'},
    {'questioncode': '0608', 'response': '102', 'displayquestionnumber': 'Q608', 'displaytext': 'TOTALS', 'displayorder': '8', 'validation_info': [{'name': 'Question vs Derived Question', 'overridden': False, 'validationoutputid': 2767, 'triggered': True, 'validationmessage': 'This total is not equal to the derived total'}], 'panel': 'panel--error'},
    {'questioncode': '9001', 'response': '2362386', 'displayquestionnumber': 'Q9001', 'displaytext': 'Derived Total of all sand and gravel (Q601 + Q602 + Q603 + Q604 + Q605 + Q606 + Q607)', 'displayorder': '9', 'validation_info': [], 'panel': 'panel--info'}]}
    assert combine_responses_and_validations(form_output, validation_output) == expected_output

def test_blank_form_blank_validation_returns_valid_output():
    expected_output = {'form_validation_outputs': [{'questioncode': '0146', 'response': '', 'displayquestionnumber': 'Q146', 'displaytext': 'Comment on the figures included in your return', 'displayorder': '11', 'validation_info': [], 'panel': ''},
    {'questioncode': '0147', 'response': '', 'displayquestionnumber': 'Q147', 'displaytext': 'New pits or quarries brought into use since date of last return', 'displayorder': '10', 'validation_info': [], 'panel': ''},
    {'questioncode': '0601', 'response': '', 'displayquestionnumber': 'Q601', 'displaytext': 'Sand produced for asphalt (asphalting sand)', 'displayorder': '1', 'validation_info': [], 'panel': ''},
    {'questioncode': '0602', 'response': '', 'displayquestionnumber': 'Q602', 'displaytext': 'Sand produced for use in mortar (building or soft sand)', 'displayorder': '2', 'validation_info': [], 'panel': ''},
    {'questioncode': '0603', 'response': '', 'displayquestionnumber': 'Q603', 'displaytext': 'Sand produced for concreting (sharp sand)', 'displayorder': '3', 'validation_info': [], 'panel': ''},
    {'questioncode': '0604', 'response': '', 'displayquestionnumber': 'Q604', 'displaytext': 'Gravel coated with bituminous binder (on or off site)', 'displayorder': '4', 'validation_info': [], 'panel': ''},
    {'questioncode': '0605', 'response': '', 'displayquestionnumber': 'Q605', 'displaytext': 'Gravel produced for concrete aggregate (including sand/gravel mixes)', 'displayorder': '5', 'validation_info': [], 'panel': ''},
    {'questioncode': '0606', 'response': '', 'displayquestionnumber': 'Q606', 'displaytext': 'Other screened and graded gravels', 'displayorder': '6', 'validation_info': [], 'panel': ''},
    {'questioncode': '0607', 'response': '', 'displayquestionnumber': 'Q607', 'displaytext': 'Sand and gravel used for constructional fill', 'displayorder': '7', 'validation_info': [], 'panel': ''},
    {'questioncode': '0608', 'response': '', 'displayquestionnumber': 'Q608', 'displaytext': 'TOTALS', 'displayorder': '8', 'validation_info': [], 'panel': ''},
    {'questioncode': '9001', 'response': '', 'displayquestionnumber': 'Q9001', 'displaytext': 'Derived Total of all sand and gravel (Q601 + Q602 + Q603 + Q604 + Q605 + Q606 + Q607)', 'displayorder': '9', 'validation_info': [], 'panel': ''}]}
    assert combine_responses_and_validations(blank_form_output, blank_validations_output) == expected_output

def test_missing_key_input_returns_key_error_json():
    with pytest.raises(KeyError):
        combine_responses_and_validations(form_output, invalid_validation_output)

def test_invalid_json_returns_type_error_json():
    with pytest.raises(TypeError):
        combine_responses_and_validations(form_output, invalid_json)

def test_blank_json_returns_error_json():
    with pytest.raises(KeyError):
        combine_responses_and_validations(form_output, empty_input_json)
