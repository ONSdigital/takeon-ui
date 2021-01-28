import json
import os
from flask import render_template, Blueprint, request, redirect, url_for, current_app, abort
from app.utilities.helpers import build_uri, get_user, question_order
from app.utilities.filter_validations import filter_validations
from app.utilities.parse_historic_data import group_historic_data
from app.utilities.combine_data import combine_responses_and_validations
from app.utilities.check_status import check_status
from app.setup import log, api_caller
from app.utilities.save_and_validate import save_form, validate
from spp_cognito_auth import requires_auth, requires_role

view_form_blueprint = Blueprint(
    name='view_form', import_name=__name__, url_prefix='/contributor_search')
url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')
form_view_template_HTML = "./view_form/FormView.html"


# Main entry-point
@view_form_blueprint.route('/Contributor/<inqcode>/<period>/<ruref>/viewform', methods=['GET', 'POST'])
@requires_auth
@requires_role(["dev", "survey.*.*"])
def view_form(inqcode, period, ruref):
    if (
        request.form
        and request.form['action'] == 'save-and-validate'
        and not current_app.auth.has_permission(["dev", "survey.*.write", "survey.*.manager"])
    ):
        abort(403)
    log.info("View_Form -- START --")

    log.info("Request.form: %s", request.form)

    try:
        status_message = ""
        url_parameters = dict(
            zip(["survey", "period", "reference"], [inqcode, period, ruref]))
        parameters = build_uri(url_parameters)

        contributor_details = api_caller.contributor_search(parameters=parameters)
        contributor_data = json.loads(contributor_details)
        log.info("Contributor Details: %s", contributor_data)
        log.info("Contributor Details[0]: %s", contributor_data['data'][0])

        validation_outputs = api_caller.validation_outputs(parameters=parameters)
        validations = json.loads(validation_outputs)
        log.info("Validations output: %s", validations)

        view_forms = api_caller.view_form_responses(parameters=parameters)
        view_form_data = json.loads(view_forms)
        log.info("View Form Data: %s", view_form_data)

        historic_data = api_caller.request_get(endpoint="/viewform/historydata", parameters=parameters).text
        historic_data_json = json.loads(historic_data)
        log.info("History Data: %s", historic_data_json)

        grouped_historic_data = group_historic_data(historic_data_json)
        log.info("Grouped Historic Data by question : %s", grouped_historic_data)

        status = contributor_data['data'][0]['status']
        status_colour = check_status(status)
        log.info("status colour: %s", status_colour)

        filtered_validations = filter_validations(validations)
        log.info("filtered validations: %s", filtered_validations)
        response_and_validations = combine_responses_and_validations(view_form_data, filtered_validations)
        log.info("response_and_validations: %s", response_and_validations)
        ordered_response_and_validations = question_order(response_and_validations, log)
        log.info("Combined Response and Validation Info Data: %s", ordered_response_and_validations)

        override_button = override_all_button(ordered_response_and_validations)
    except Exception as error:
        log.info("Error %s", error)

    log.info("Filtered Validations output: %s",
             filter_validations(validations))

    if request.form and request.form['action'] == 'save-and-validate':
        save_form(parameters, request.form, inqcode, period, ruref)
        validate(inqcode, period, ruref)
        return redirect(url_for('view_form.view_form', inqcode=inqcode, period=period, ruref=ruref))

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
        historic_data=historic_data_json,
        grouped_historic_data=grouped_historic_data)


@view_form_blueprint.route('/Contributor/<inqcode>/<period>/<ruref>/override-validations', methods=['POST'])
@requires_auth
@requires_role(["dev", "survey.*.write", "survey.*.manager"])
def override_validations(inqcode, period, ruref):
    json_data = request.json
    log.info("Checkbox checked data: %s", str(json_data))
    ruref = json_data['reference']
    inqcode = json_data['survey']
    period = json_data['period']

    api_caller.validation_overrides(parameters='', data=json.dumps(json_data))
    log.info("Overriding Validations...")
    return redirect(url_for('view_form.view_form', inqcode=inqcode, period=period, ruref=ruref))


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
