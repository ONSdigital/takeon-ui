from app.utilities.filter_validations import filter_validations


def test_filter_validations_onetrueonefalse_outputonetrue():
    input_dict = {'validation_outputs': [{'severity': 'W', 'primaryquestion': '0601', 'triggered': False,
                                          'instance': '0', 'validationoutputid': 69, 'validationid': 6610,
                                          'lastupdateddate': None,
                                          'lastupdatedby': None, 'name': 'Period on Period Movement',
                                          'formula': 'abs(2335 - 0) > 20000 AND 2335 > 0 AND 0 > 0', 'rule': 'POPM', 'overridden': False},
                                         {'severity': 'E', 'primaryquestion': '0601', 'triggered': True,
                                          'instance': '0', 'validationoutputid': 76, 'validationid': 6620,
                                          'lastupdateddate': '2020-02-11T12:18:02.242+00:00',
                                          'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity',
                                          'formula': '2335 != 0 AND ( 2335 = 0 OR 0 = 0 ) AND abs(2335 - 0) > 0', 'rule': 'POPZC', 'overridden': True}]}
    expected_output = {'validation_outputs': [{'severity': 'E', 'primaryquestion': '0601', 'triggered': True,
                                               'instance': '0', 'validationoutputid': 76, 'validationid': 6620,
                                               'lastupdateddate': '2020-02-11T12:18:02.242+00:00',
                                               'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity',
                                               'formula': '2335 != 0 AND ( 2335 = 0 OR 0 = 0 ) AND abs(2335 - 0) > 0', 'rule': 'POPZC', 'overridden': True}]}
    assert filter_validations(input_dict) == expected_output


def test_filter_validations_twotrue_outputtwotrue():
    input_dict = {'validation_outputs': [{'severity': 'W', 'primaryquestion': '0601', 'triggered': True,
                                          'instance': '0', 'validationoutputid': 69, 'validationid': 6610,
                                          'lastupdateddate': None,
                                          'lastupdatedby': None, 'name': 'Period on Period Movement',
                                          'formula': 'abs(2335 - 0) > 20000 AND 2335 > 0 AND 0 > 0', 'rule': 'POPM', 'overridden': False},
                                         {'severity': 'E', 'primaryquestion': '0601', 'triggered': True,
                                          'instance': '0', 'validationoutputid': 76, 'validationid': 6620,
                                          'lastupdateddate': '2020-02-11T12:18:02.242+00:00',
                                          'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity',
                                          'formula': '2335 != 0 AND ( 2335 = 0 OR 0 = 0 ) AND abs(2335 - 0) > 0', 'rule': 'POPZC', 'overridden': True}]}
    expected_output = {'validation_outputs': [{'severity': 'W', 'primaryquestion': '0601', 'triggered': True,
                                               'instance': '0', 'validationoutputid': 69, 'validationid': 6610,
                                               'lastupdateddate': None,
                                               'lastupdatedby': None, 'name': 'Period on Period Movement',
                                               'formula': 'abs(2335 - 0) > 20000 AND 2335 > 0 AND 0 > 0', 'rule': 'POPM', 'overridden': False},
                                              {'severity': 'E', 'primaryquestion': '0601', 'triggered': True,
                                               'instance': '0', 'validationoutputid': 76, 'validationid': 6620,
                                               'lastupdateddate': '2020-02-11T12:18:02.242+00:00',
                                               'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity',
                                               'formula': '2335 != 0 AND ( 2335 = 0 OR 0 = 0 ) AND abs(2335 - 0) > 0', 'rule': 'POPZC', 'overridden': True}]}
    assert filter_validations(input_dict) == expected_output


def test_filter_validations_twofalse_outputempty():
    input_dict = {'validation_outputs': [{'severity': 'W', 'primaryquestion': '0601', 'triggered': False,
                                          'instance': '0', 'validationoutputid': 69, 'validationid': 6610,
                                          'lastupdateddate': None,
                                          'lastupdatedby': None, 'name': 'Period on Period Movement',
                                          'formula': 'abs(2335 - 0) > 20000 AND 2335 > 0 AND 0 > 0', 'rule': 'POPM', 'overridden': False},
                                         {'severity': 'E', 'primaryquestion': '0601', 'triggered': False,
                                          'instance': '0', 'validationoutputid': 76, 'validationid': 6620,
                                          'lastupdateddate': '2020-02-11T12:18:02.242+00:00',
                                          'lastupdatedby': 'fisdba', 'name': 'Period on Period Zero Continuity',
                                          'formula': '2335 != 0 AND ( 2335 = 0 OR 0 = 0 ) AND abs(2335 - 0) > 0', 'rule': 'POPZC', 'overridden': True}]}
    expected_output = {'validation_outputs': []}
    assert filter_validations(input_dict) == expected_output
