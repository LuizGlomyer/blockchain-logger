from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import AccessSchema

from utils.utils import receipt_deserializer
from utils.logger import Logger, UserInteractions

blp = Blueprint("Access", "access", description="System login and logout")
logger = Logger("access")

    
@blp.route("/access/login/")
class Access(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.LOGIN)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    

@blp.route("/access/logoff/")
class Access(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.LOGOFF)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"status": deserialized_receipt["status"], "sentData": item_data, "receipt": deserialized_receipt}
