import json

from urllib.error import URLError

# from content_management import Content
from flask import (
    request,
    Blueprint,
    redirect,
    url_for,
    render_template,
    render_template_string,
    jsonify,
)
from flask_jwt_extended import jwt_required

from app.utilities.helpers import (
    create_form_class,
    create_new_dict,
    clean_search_parameters,
    build_uri,
    build_links,
)
from app.utilities.graphql_data import GraphData
from app.setup import discovery_service

contributor_search_blueprint = Blueprint(
    name="contributor_search", import_name=__name__, url_prefix="/contributor_search"
)

contributor_search_blueprint_post = Blueprint(
    name="contributor_search_post",
    import_name=__name__,
    url_prefix="/contributor_search",
)

# headers here double as url parameters
headers = ["reference", "period", "survey", "status", "formId"]


#################################################################################################
# ######################################## FLASK ENDPOINTS ######################################
#################################################################################################
@contributor_search_blueprint.errorhandler(404)
def not_found(e):
    return render_template("./error_templates/404.html", message_header=e), 404


@contributor_search_blueprint.errorhandler(403)
def not_auth(e):
    return render_template("./error_templates/403.html", message_header=e), 403


@contributor_search_blueprint.errorhandler(500)
def internal_server_error(e):
    return render_template("./error_templates/500.html", message_header=e), 500


@contributor_search_blueprint.route("/")
# Redirect to from the landing page to the GeneralSearchScreen
def landing_page():
    return redirect(url_for("contributor_search.general_search_screen_selection"))


# ####################### SIMPLE SEARCH SCREEN, EXPOSES ALL FIELDS #############################
@contributor_search_blueprint.route(
    "/Contributor/searchSelection", methods=["GET", "POST"]
)
# @jwt_required
# Selection options, just pull out the values that have been selected, join
# them all together in a semi-colon delimited string
def general_search_screen_selection():
    if request.method == "POST":
        criteria = ";".join(i for i in request.form.keys())
        # redirect to general search screen, criteria is added as a url parameter. ?criteria=VALUE1;VALUE2
        return redirect(
            url_for("contributor_search.general_search_screen", criteria=criteria)
        )

    return render_template("./search_screen_choice/GeneralSearchScreenChoice.html")


@contributor_search_blueprint.route("/Contributor/GeneralSearch", methods=["POST"])
def general_search_screen_post():
    print("Reached post")
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
    url_connect += ";first=10"
    print("url connect: {}".format(url_connect))

    data = GraphData(
        discovery_service.contributor_search(url_connect, "business-layer")
    )
    output_data = data.nodes
    # links = data.page_info
    return render_template(
        "./contributor_search/GeneralSearchScreenGQL.html",
        form=form,
        records=output_data,
        header=output_data[0],
        fields=dict(form.__dict__["_fields"]),
        links=data.page_info,
    )


@contributor_search_blueprint.route("/Contributor/next", methods=["POST"])
def next_page():
    newpage = request.json["cursor"]
    url_connect = "graphql;" + f";startCursor={newpage}" + ";first=10"
    print(newpage)
    data = GraphData(
        discovery_service.graphql_post(url_connect, "business-layer")
    )

    print(data.nodes)
    output_data = data.nodes
    links = data.page_info
    return jsonify(data=output_data, links=links)


@contributor_search_blueprint.route("/Contributor/previous", methods=["POST"])
def previous_page():
    newpage = request.json["cursor"]
    url_connect = "graphql;" + f";endCursor={newpage}" + ";last=10"
    print(newpage)
    data = GraphData(
        discovery_service.graphql_post(url_connect, "business-layer")
    )

    print(data.nodes)
    output_data = data.nodes
    links = data.page_info
    return jsonify(data=output_data, links=links)

@contributor_search_blueprint.route("/Contributor/GeneralSearch", methods=["GET"])
# Main search screen
def general_search_screen():
    criteria = request.args["criteria"].split(";")
    # Build class for the forms that are passed in, this must be done dynamically
    selection_form = create_form_class(criteria)
    # create form object
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
