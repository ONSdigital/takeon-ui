from flask import Blueprint

healtchecks_blueprint = Blueprint(
    name='healthchecks', import_name=__name__, url_prefix='/health')


@healtchecks_blueprint.route('/status', methods=['GET', 'POST'])
def health_check():
    return 'Container is healthy'
