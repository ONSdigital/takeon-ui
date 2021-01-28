from flask import redirect, url_for, render_template, Blueprint, request
from spp_cognito_auth import requires_auth, requires_role
from app.setup import log

search_screen_choice_blueprint = Blueprint(name='search_selection', import_name=__name__)


#################################################################################################
# ######################################## FLASK ENDPOINTS ######################################
#################################################################################################

@search_screen_choice_blueprint.route('/', methods=['GET', 'POST'])
@requires_auth
@requires_role(["dev"])
def general_search_screen_selection():
    if request.method == "POST":
        log.info(request.form)
        criteria = ';'.join(i for i in request.form.keys())
        return redirect(url_for("contributor_search.general_search_screen", criteria=criteria))
    return render_template('./search_screen_choice/GeneralSearchScreenChoice.html')
