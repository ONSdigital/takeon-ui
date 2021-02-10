import json
import os
import time
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
        html_text = return_html()
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
        time.sleep(5)
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
        grouped_historic_data=grouped_historic_data,
        html_text=html_text)

    


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


def return_html():
    html = """
    <!doctype html>
        <html lang="en-gb" dir="ltr" class="no-js">
        <head>
            {% block head %}
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title></title>
            <link rel="stylesheet" href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/css/main.css">
            <meta name="msapplication-config"
                content="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/browserconfig.json">
            <link rel="icon" type="image/x-icon" href="https://cdn.ons.gov.uk/sdc/design-system/24.0.1/favicons/favicon.ico">
            <link rel="icon" type="image/png"
                href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/favicon-32x32.png" sizes="32x32">
            <link rel="icon" type="image/png"
                href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/favicon-16x16.png" sizes="16x16">
            <link rel="mask-icon" color="#5BBAD5"
                href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/safari-pinned-tab.svg">
            <link rel="apple-touch-icon" type="image/png"
                href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/apple-touch-icon.png" sizes="180x180">
            <link rel="manifest" href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/manifest.json">

                {% block css %}
                    <link rel="stylesheet" href="https://cdn.ons.gov.uk/sdc/design-system/16.1.0/css/main.css" media="all"
                        type="text/css">
                    <link rel="stylesheet" href="{{ url_for('static',filename='css/custom.css') }}" media="all" type="text/css">
                {% endblock css %}

                {% block head_js %}
                    <script>var ONS_assets_base_URL='https://cdn.ons.gov.uk/sdc/design-system/24.0.3/';</script>
                    <script src="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/scripts/main.js"></script>

                    <script type="text/javascript"
                            src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
                    <script type="text/javascript" src="{{ url_for('static', filename='js/industry-range.js') }}"></script>
                {% endblock head_js %}

            {% endblock head %}

        </head>

        <body>
        <div class="phase-banner mainContent">
            <div class="grid grid--flex grid--gutterless grid--vertical-center grid--no-wrap">
                <div class="grid__col col-auto u-flex-no-grow">
                    <h3 class="phase-banner__badge">BETA</h3>
                </div>
                <div class="grid__col col-auto u-flex-shrink">
                    <p class="phase-banner__desc u-fs-s u-mb-no">This is a work in progress</p>
                </div>
            </div>
        </div>

        <header class="header header--internal header--thin">
            <div class="header__top mainContent" role="banner">
                <div class="header__grid-top grid grid--gutterless grid--flex grid--between grid--vertical-center grid--no-wrap">
                    <div class="grid__col col-auto">
                        <a class="header__logo-link" href="/">
                            <img class="header__logo" src="{{ url_for('static',filename='img/ons-logo-white.svg') }}"
                                alt="Office for National Statistics logo">
                        </a>
                    </div>
                </div>
            </div>
            <div class="header__main">
                <div class="grid grid--gutterless grid--flex grid--between grid--vertical-center grid--no-wrap mainContent">
                    <div class="grid__col col-auto u-flex-shrink">
                        <div class="header__title">
                            {% block page_header %}
                            {% endblock page_header %}
                        </div>
                    </div>

                    <div class="grid__col col-auto u-flex-no-shrink u-d-no@xs@m">
                        <a href="{{ url_for('auth.logout') }}" role="button" class="btn btn--ghost u-d-no@xs@m btn--exit">
                        <span class="btn__inner">Sign out
                            <svg class="svg-icon" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13.85,7.65l-2.5-2.5a.5.5,0,0,0-.71,0,.48.48,0,0,0-.15.36V7h-3a.5.5,0,0,0-.5.5v1a.5.5,0,0,0,.5.5h3v1.5A.49.49,0,0,0,11,11a.48.48,0,0,0,.34-.14l2.51-2.5a.49.49,0,0,0,0-.68Z" transform="translate(-2 -2)" />
                            <path d="M8.5,14h-6a.5.5,0,0,1-.5-.5V2.5A.5.5,0,0,1,2.5,2h6a.5.5,0,0,1,.5.5V3a.5.5,0,0,1-.5.5h-5v9h5A.5.5,0,0,1,9,13v.5A.5.5,0,0,1,8.5,14Z" transform="translate(-2 -2)" />
                            </svg>
                        </span>
                        </a>
                    </div>
                </div>
            </div>
        </header>

        {% block content %}

            <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script> -->
            
            <div class="mainContent">
                <main class="page__main">
                    <h1>Updating Contributor Details, Please Wait</h1>
                </main>
            </div>

        {% endblock content %}

        <footer class="footer " data-ga-element="footer">
            <div class="container">
                <div class="grid">
                    <div class="grid__col col-4@m">
                        <!-- Footer text here -->
                    </div>
                    <div class="grid__col u-mt-m u-mb-m">
                        <hr class="footer__hr">
                    </div>
                    <div class="grid__col">
                        <div class="footer__license">
                            <img alt="OGL" class="footer__ogl-img"
                                src="{{ url_for('static',filename='img/UKOpenGovernmentLicence-grey.svg') }}">
                            All content is available under the <a
                                href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
                                class="footer__link">Open Government Licence v3.0</a>, except where otherwise stated
                        </div>
                    </div>
                </div>
            </div>
        </footer>

        </body>

        </html>
    """

    return html