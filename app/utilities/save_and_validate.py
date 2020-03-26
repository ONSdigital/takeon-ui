def save_form(parameters, requestform, inqcode, period, ruref):
    try:
        response_data = extract_responses(requestform)
        log.info('Response data: %s', response_data)
        # Build up JSON structure to save
        json_output = {}
        json_output["responses"] = response_data
        json_output["user"] = get_user()
        json_output["reference"] = ruref
        json_output["period"] = period
        json_output["survey"] = inqcode

        # Send the data to the business layer for processing
        log.info("Output JSON: %s", str(json_output))
        api_caller.save_response(parameters=parameters, data=json_output)
        status_message = 'Responses saved successfully'
        return status_message
    except HTTPError as http_error:
        status_message = 'There was a problem with the HTTP call ' + http_error
        log.info('HTTP Error %s', http_error)
    except ConnectionError as connection_error:
        status_message = 'There was a problem with the connection ' + connection_error
        log.info('Connection Error %s', connection_error)
    except Timeout as timeout_error:
        status_message = 'Timeout error ' + timeout_error
        log.info('Timeout Error %s', timeout_error)
    except RequestException as requests_error:
        status_message = 'There was a problem with your request ' + requests_error + 'Please contact Take-On Support Team'
        log.info('Requests Error: %s', requests_error)

def validate(inqcode, period, ruref, response_and_validations, override_button, contributor_data, validations, status_colour):
    log.info('save validation button pressed')
    json_data = {"survey": inqcode, "period": period,
                 "reference": ruref, "bpmId": "0"}
    header = {"x-api-key": api_key}
    status_message = 'Validation Run Successfully'
    try:
        response = api_caller.run_validation(
            url, json.dumps(json_data), header)
        log.info("Response from SQS: %s", response)
    except HTTPError as http_err:
        status_message = "Http Error. Unable to call URL"
        log.info('URL error occurred: %s', http_err)
    except ConnectionError as connection_err:
        status_message = "Connection Error. Unable to Connect to API Gateway"
        log.info('API request error occured: %s', connection_err)
    except Exception as e:
        status_message = 'Validation Error. Kubernetes secret does not exist or is incorrect'
        log.info('Validation Error Occurred: %s', e)
        return render_template(
            template_name_or_list="./error_templates/validate_error.html",
            error=e
        )
    return render_template(
        template_name_or_list=form_view_template_HTML,
        survey=inqcode,
        period=period,
        ruref=ruref,
        data=response_and_validations,
        override_button=override_button,
        status_message=json.dumps(status_message),
        contributor_details=contributor_data['data'][0],
        validation=filter_validations(validations),
        status_colour=status_colour)