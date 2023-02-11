from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import AccessSchema
from blockchain.main import blockchain_connection

from utils.utils import receipt_deserializer
from utils.logger import Logger

blp = Blueprint("Reports", "reports", description="Reports of blockchain-stored logs")

logger = Logger("reports")


@blp.route("/reports/<string:user_id>") 
class View(MethodView):
    @blp.response(200)
    def get(cls, user_id):
        try:
            value = blockchain_connection.fetch_items(user_id)
            return {"logs":value, "id": user_id}
        except KeyError:
            abort(404, message="Not found.")
