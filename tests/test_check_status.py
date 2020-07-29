from app.utilities.check_status import check_status


def test_check_status_clear_success():
    input_status = 'Clear'
    output = 'status status--success'
    assert check_status(input_status) == output


def test_check_status_blank_default():
    input_status = ''
    output = 'status status--info'
    assert check_status(input_status == output)
