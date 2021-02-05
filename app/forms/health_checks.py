from flask import Flask

app = Flask(__name__)
# healtchecks_blueprint = Blueprint(
#     name='health_checks', import_name=__name__, url_prefix='/health')


# @healtchecks_blueprint.route('/status', methods=['GET', 'POST'])
app.route("/health")
def health_check():
    return 'Container is healthy'
