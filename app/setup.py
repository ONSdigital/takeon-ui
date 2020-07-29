import logging
from flask import Flask
from app import settings
from app.utilities.api_request import ApiRequest

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

api_caller = ApiRequest(service="business-layer", mocking=settings.MOCKING)
api_caller_pl = ApiRequest(service="persistence-layer", mocking=settings.MOCKING)


def create_app(setting_overrides=None):
    # Define the WSGI application object
    application = Flask(__name__, static_url_path='/s', static_folder='./static')

    # Configurations
    application.config.from_object(settings)
    application.config['JWT_TOKEN_LOCATION'] = ['cookies']  # store token in cookies
    application.config['JWT_COOKIE_SECURE'] = True  # cookies can only be sent over https
    application.config['JWT_ACCESS_COOKIE_PATH'] = ''
    application.config['JWT_SECRET_KEY'] = settings.SECRET_KEY  # using default secret key
    application.config['CORS_HEADERS'] = 'Content-Type'

    if setting_overrides:
        application.config.update(setting_overrides)

    add_blueprints(application)
    return application


def add_blueprints(application):

    from app.forms.contributor_search_form import contributor_search_blueprint, contributor_search_blueprint_post
    application.register_blueprint(contributor_search_blueprint)
    application.register_blueprint(contributor_search_blueprint_post)
    contributor_search_blueprint_post.config = application.config.copy()
    contributor_search_blueprint.config = application.config.copy()

    from app.forms.view_form import view_form_blueprint
    application.register_blueprint(view_form_blueprint)
    view_form_blueprint.config = application.config.copy()

    from app.forms.search_screen_choice import search_screen_choice_blueprint
    application.register_blueprint(search_screen_choice_blueprint)
    search_screen_choice_blueprint.config = application.config.copy()

    from app.forms.login_form import login_form_blueprint
    application.register_blueprint(login_form_blueprint)
    login_form_blueprint.config = application.config.copy()
