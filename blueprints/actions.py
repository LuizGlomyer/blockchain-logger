from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import AccessSchema

from utils.utils import receipt_deserializer, build_response
from utils.logger import Logger, UserInteractions

blp = Blueprint("Actions", "actions", description="User-made actions on the system")
logger = Logger("actions")


@blp.route("/actions/buy-ticket/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.BUY_TICKET)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/select-ticket/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.SELECT_TICKET)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/actions/pix-payment/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.PIX_PAYMENT)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
