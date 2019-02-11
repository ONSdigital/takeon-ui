from flask import Blueprint, redirect, render_template, request, url_for
from flask_jwt_extended import set_access_cookies
from app.utilities.helpers import create_form_class
from app.auth import build_headers, build_payload, get_token
from app.settings import TOKEN_ENDPOINT, CLIENT_ID, CLIENT_SECRET

login_form_blueprint = Blueprint(name='login_form', import_name=__name__)


@login_form_blueprint.route('/login', methods=['GET', 'POST'])
def login_form():
    login = create_form_class(['Username', 'Password'])
    form = login(request.form)  # create form object

    if request.method == "POST" and form.validate():
        print(request.form)

        raw_token = get_token(TOKEN_ENDPOINT,
                              build_payload(request.form['Username'], request.form['Password']),
                              build_headers(CLIENT_ID, CLIENT_SECRET))
        token = raw_token.json()
        access_token = token['access_token']

        resp = redirect(url_for('contributor_search.general_search_screen_selection'))
        set_access_cookies(resp, access_token)
        return resp

    return render_template("./login_form/FormLogin.html", form=form, fields=dict(form.__dict__['_fields']))
