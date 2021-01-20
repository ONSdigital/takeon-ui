import logging
import os
from flask import Flask, session, render_template
from app import settings
from app.utilities.api_request import ApiRequest
from werkzeug.middleware.proxy_fix import ProxyFix
import immutables
import sys
from uuid import uuid4

from spp_cognito_auth import Auth, AuthConfig, AuthBlueprint, new_oauth_client
from spp_logger import SPPLogger, SPPLoggerConfig

def set_logger(lambda_name, context, survey, period):
    # get log level from ENV VAR and convert to upper case
    log_level = os.getenv("LOG_LEVEL", default="INFO").upper()
    # set logger configs
    config = SPPLoggerConfig(
        service="Data Clearing UI",
        component="Data Clearing UI",
        environment="dev",
        deployment="dev"
    )
    try:
        logger = SPPLogger(
            name="dc_ui_logger",
            config=config,
            context=immutables.Map(
                log_level=log_level,
                log_correlation_id=str(uuid4())
            ),
            stream=sys.stdout,
        )
    except Exception as error:
        logger = logging.getLogger()
        logger.error("Failed to instantiate SPPLogger", exc_info=error)
    return logger


# log = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)
log = set_logger("lambda_name", "context", "survey", "period")

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
    application.config["SESSION_COOKIE_SECURE"] = os.getenv(
        "SESSION_COOKIE_SECURE", False
    )
    application.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

    if setting_overrides:
        application.config.update(setting_overrides)

    auth_config = AuthConfig.from_env()
    oauth_client = new_oauth_client(auth_config)
    application.auth = Auth(auth_config, oauth_client, session)

    add_error_handlers(application)
    add_blueprints(application)

    # Run with proxyfix when behind ELB as SSL is done at the load balancer
    if application.config["SESSION_COOKIE_SECURE"]:
        return ProxyFix(application, x_for=1, x_host=1)
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

    application.register_blueprint(AuthBlueprint().blueprint())


def add_error_handlers(application):
    @application.errorhandler(404)
    def not_found(error):
        return render_template('./error_templates/404.html', message_header=error), 404

    @application.errorhandler(403)
    def not_auth(error):
        return render_template('./error_templates/403.html', message_header=error), 403

    @application.errorhandler(500)
    def internal_server_error(error):
        return render_template('./error_templates/500.html', message_header=error), 500

