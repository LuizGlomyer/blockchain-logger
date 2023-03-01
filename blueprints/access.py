from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import AccessSchema

from utils.utils import receipt_deserializer, build_response
from utils.logger import Logger, UserInteractions

blp = Blueprint("Access", "access", description="System login and logout")
logger = Logger("access")


@blp.route("/access/create-user/")
class Access(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.CREATE_USER)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)

    
@blp.route("/access/login/")
class Access(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.LOGIN)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/access/logoff/")
class Access(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.LOGOFF)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
