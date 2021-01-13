from flask import (
    request,
    Blueprint,
    redirect,
    url_for,
    render_template,
    jsonify
)

from app.utilities.helpers import (
    create_form_class,
    create_new_dict,
    clean_search_parameters,
    build_uri
)
from app.utilities.graphql_data import GraphData
from app.setup import log, api_caller
from app.utilities.api_request import TakeonApiException

from spp_cognito_auth import requires_auth, requires_role

contributor_search_blueprint = Blueprint(name="contributor_search", import_name=__name__, url_prefix="/contributor_search")
contributor_search_blueprint_post = Blueprint(name="contributor_search_post", import_name=__name__, url_prefix="/contributor_search")
error_500 = "./error_templates/500.html"

# headers here double as url parameters
headers = ["reference", "period", "survey", "status", "formId"]


#################################################################################################
# ######################################## FLASK ENDPOINTS ######################################
#################################################################################################

@contributor_search_blueprint.errorhandler(TakeonApiException)
def handle_invalid_usage(error):
    display = 'Service Error. Please contact support'
    log.info('Exception caught: %s', error.message)
    return render_template(error_500, message_header=display), 400


@contributor_search_blueprint.app_errorhandler(Exception)
def handle_unexpected_error(error):
    log.info('Unexpected exception caught: %s', error)
    display = 'Unexpected service Error! Please contact support'
    return render_template(error_500, message_header=display), 500


@contributor_search_blueprint.route("/")
# Redirect to from the landing page to the GeneralSearchScreen
def landing_page():
    return redirect(url_for("contributor_search.general_search_screen_selection"))


# ####################### SIMPLE SEARCH SCREEN, EXPOSES ALL FIELDS #############################
@contributor_search_blueprint.route("/Contributor/searchSelection", methods=["GET", "POST"])
# Selection options, just pull out the values that have been selected, join
# them all together in a semi-colon delimited string
@requires_auth
@requires_role(["dev"])
def general_search_screen_selection():
    log.info("general_search_screen_selection")
    if request.method == "POST":
        criteria = ";".join(i for i in request.form.keys())
        # redirect to general search screen, criteria is added as a url parameter. ?criteria=VALUE1;VALUE2
        return redirect(url_for("contributor_search.general_search_screen", criteria=criteria))

    return render_template("./search_screen_choice/GeneralSearchScreenChoice.html")


@contributor_search_blueprint.route("/Contributor/GeneralSearch", methods=["POST"])
@requires_auth
@requires_role(["dev"])
def general_search_screen_post():
    log.info("general_search_screen_post")
    criteria = request.args["criteria"].split(";")

    # Build class for the forms that are passed in, this must be done dynamically
    # create form object

    # Build class for the forms that are passed in, this must be done dynamically
    selection_form = create_form_class(criteria)

    # create form object
    form = selection_form(request.form)
    mutable_form = create_new_dict(request.form)
    clean_parameters = clean_search_parameters(mutable_form)

    url_connect = build_uri(clean_parameters)
    parameters = url_connect
    url_connect += ";first=10"
    print("url connect: {}".format(url_connect))

    contributor_data = api_caller.contributor_search(parameters=url_connect)
    data = GraphData(contributor_data)
    output_data = data.nodes
    log.info("Data from GraphQL for search: %s", output_data)

    return render_template(
        "./contributor_search/GeneralSearchScreenGQL.html",
        form=form,
        records=output_data,
        header=output_data[0],
        fields=dict(form.__dict__["_fields"]),
        links=data.page_info,
        parameters=parameters
    )


@contributor_search_blueprint.route("/Contributor/next", methods=["POST"])
@requires_auth
@requires_role(["dev"])
def next_page():
    log.info("Next page")
    newpage = request.json["cursor"]
    search_parameters = request.json["search_params"]
    parameters = "graphql;" + f";startCursor={newpage}" + f";{search_parameters}" + ";first=10"
    return change_page(parameters)


@contributor_search_blueprint.route("/Contributor/previous", methods=["POST"])
@requires_auth
@requires_role(["dev"])
def previous_page():
    log.info("Previous page")
    newpage = request.json["cursor"]
    search_parameters = request.json["search_params"]
    parameters = "graphql;" + f";endCursor={newpage}" + f";{search_parameters}" + ";last=10"
    return change_page(parameters)


def change_page(parameters):
    contributor_data = api_caller.graphql_post(parameters=parameters)
    data = GraphData(contributor_data)
    output_data = data.nodes
    links = data.page_info
    return jsonify(data=output_data, links=links)


@contributor_search_blueprint.route("/Contributor/GeneralSearch", methods=["GET"])
# Main search screen
@requires_auth
@requires_role(["dev"])
def general_search_screen():

    log.info("general_search_screen")
    criteria = request.args["criteria"].split(";")

    # Build class for the forms that are passed in, this must be done dynamically
    selection_form = create_form_class(criteria)
    form = selection_form(request.form)

    # On search, and if form object passes validation enter block
    current_page = -1
    last_page = -1

    # before any searches are done, return just the webpage with the search fields.
    return render_template(
        "./contributor_search/GeneralSearchScreen.html",
        form=form,
        fields=dict(form.__dict__["_fields"]),
        current_page=current_page,
        last_page=last_page,
    )
