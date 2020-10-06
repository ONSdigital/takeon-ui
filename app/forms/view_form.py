import json
import os
from flask import render_template, Blueprint, request, redirect, url_for
from app.utilities.helpers import build_uri, get_user, question_order
from app.utilities.filter_validations import filter_validations
from app.utilities.combine_data import combine_responses_and_validations
from app.utilities.check_status import check_status
from app.setup import log, api_caller
from app.utilities.save_and_validate import save_form, validate

view_form_blueprint = Blueprint(
    name='view_form', import_name=__name__, url_prefix='/contributor_search')
url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')
form_view_template_HTML = "./view_form/FormView.html"

# Flask Endpoints
@view_form_blueprint.errorhandler(404)
def not_found(error):
    return render_template('./error_templates/404.html', message_header=error), 404


@view_form_blueprint.errorhandler(403)
def not_auth(error):
    return render_template('./error_templates/403.html', message_header=error), 403


@view_form_blueprint.errorhandler(500)
def internal_server_error(error):
    return render_template('./error_templates/500.html', message_header=error), 500

# Main entry-point
@view_form_blueprint.route('/Contributor/<inqcode>/<period>/<ruref>/viewform', methods=['GET', 'POST'])
def view_form(inqcode, period, ruref):
    log.info("View_Form -- START --")

    log.info("Request.form: %s", request.form)

    status_message = ""
    url_parameters = dict(
        zip(["survey", "period", "reference"], [inqcode, period, ruref]))
    parameters = build_uri(url_parameters)

    contributor_details = api_caller.contributor_search(parameters=parameters)
    validation_outputs = api_caller.validation_outputs(parameters=parameters)
    view_forms = api_caller.view_form_responses(parameters=parameters)

    historic_data = api_caller.request_get(endpoint="/viewform/historydata", parameters=parameters).text
    historic_data_json = json.loads(historic_data)
    historic_questions = historic_data['history_data'][0]['view_form_responses']

    historic_questions_list = []
    for row in historic_questions:
        historic_questions_list.append(row['questioncode'])

    contributor_data = json.loads(contributor_details)
    validations = json.loads(validation_outputs)
    status = contributor_data['data'][0]['status']
    status_colour = check_status(status)

    view_form_data = json.loads(view_forms)

    response_and_validations = combine_responses_and_validations(view_form_data, filter_validations(validations))
    ordered_response_and_validations = question_order(response_and_validations) 
    override_button = override_all_button(ordered_response_and_validations)

    log.info("Contributor Details: %s", contributor_data)
    log.info("Contributor Details[0]: %s", contributor_data['data'][0])
    log.info("View Form Data: %s", view_form_data)
    log.info("Validations output: %s", validations)
    log.info("Filtered Validations output: %s",
             filter_validations(validations))
    log.info("Combined Response and Validation Info Data: %s", ordered_response_and_validations)
    log.info("History Data: %s", historic_data_json)

    if request.form and request.form['action'] == 'save-and-validate':
        save_form(parameters, request.form, inqcode, period, ruref)
        validate(inqcode, period, ruref, ordered_response_and_validations, override_button, contributor_data, validations, status_colour)

    return render_template(
        template_name_or_list=form_view_template_HTML,
        survey=inqcode,
        period=period,
        ruref=ruref,
        data=ordered_response_and_validations,
        override_button=override_button,
        status_message=json.dumps(status_message),
        contributor_details=contributor_data['data'][0],
        validation=filter_validations(validations),
        user=get_user(),
        status_colour=status_colour,
        # historic_data=historic_data_json['history_data'])
        historic_data=historic_data_json,
        historic_question_numbers=historic_questions_list)


@view_form_blueprint.route('/Contributor/<inqcode>/<period>/<ruref>/override-validations', methods=['POST'])
def override_validations(inqcode, period, ruref):
    json_data = request.json
    log.info("Checkbox checked data: %s", str(json_data))
    ruref = json_data['reference']
    inqcode = json_data['survey']
    period = json_data['period']

    api_caller.validation_overrides(parameters='', data=json.dumps(json_data))
    log.info("Overriding Validations...")

    return redirect(url_for(view_form, inqcode=inqcode, period=period, ruref=ruref))

def extract_responses(data) -> dict:
    output = []
    for key in data.keys():
        if key != "action" and key != "override-checkbox":
            output.append({'question': key, 'response': data[key], 'instance': 0})
    return output

def override_all_button(data):
    validation_triggered_counter = 0
    for row in data['form_validation_outputs']:
        if row['validation_info']:
            validation_triggered_counter += 1
        if validation_triggered_counter == 2:
            return True
    return False
