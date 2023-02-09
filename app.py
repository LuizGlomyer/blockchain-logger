from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_smorest import Api

from blueprints.access import blp as AccessBlueprint
from blueprints.view import blp as ViewBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "RU Blockchain API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(AccessBlueprint)
api.register_blueprint(ViewBlueprint)