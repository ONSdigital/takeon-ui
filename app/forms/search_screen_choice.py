from flask import redirect, url_for, render_template, Blueprint, request

search_screen_choice_blueprint = Blueprint(name='search_selection', import_name=__name__)


#################################################################################################
# ######################################## FLASK ENDPOINTS ######################################
#################################################################################################
@search_screen_choice_blueprint.errorhandler(404)
def not_found(error):
    return render_template('./error_templates/404.html', message_header=error), 404


@search_screen_choice_blueprint.errorhandler(403)
def not_auth(error):
    return render_template('./error_templates/403.html', message_header=error), 403


@search_screen_choice_blueprint.errorhandler(500)
def internal_server_error(error):
    return render_template('./error_templates/500.html', message_header=error), 500


@search_screen_choice_blueprint.route('/', methods=['GET', 'POST'])
def general_search_screen_selection():
    if request.method == "POST":
        print(request.form)
        criteria = ';'.join(i for i in request.form.keys())
        return redirect(url_for("contributor_search.general_search_screen", criteria=criteria))
    return render_template('./search_screen_choice/GeneralSearchScreenChoice.html')
