def check_status(status):
    status_code = {
        'No form sent'          : 'status status--dead',
        'Form sent out'         : 'status status--info',
        'Saved - run validation': 'status status--error',
        'Check needed'          : 'status status--error',
        'Clear'                 : 'status status--success',
        'Clear - overridden'    : 'status status--success'
    }
    return status_code.get(status, 'status status--info')
