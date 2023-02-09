from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import AccessSchema
from blockchain.main import Connection

from utils.utils import receipt_deserializer
from utils.logger import Logger, Actions

blp = Blueprint("View", "view", description="Visualizing system data")
blockchain = Connection()
logger = Logger("view")

@blp.route("/view/<string:user_id>") 
class View(MethodView):
    @blp.response(200)
    def get(cls, user_id):
        try:
            value = blockchain.fetch_items(user_id)
            return {"id":value, "name": "nome", "teste":1}
        except KeyError:
            abort(404, message="Not found.")
    
    
@blp.route("/view/login/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        log_message = logger.format_log(item_data["name"], Actions.LOGIN)
        receipt = blockchain.create_item(item_data["id"], log_message)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    

@blp.route("/view/data/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        log_message = logger.format_log(item_data["name"], Actions.VIEW_DATA)
        receipt = blockchain.create_item(item_data["id"], log_message)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    

@blp.route("/view/ticket-list/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        log_message = logger.format_log(item_data["name"], Actions.VIEW_TICKET_LIST)
        receipt = blockchain.create_item(item_data["id"], log_message)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    

@blp.route("/view/ticket-history/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        log_message = logger.format_log(item_data["name"], Actions.VIEW_TICKET_HISTORY)
        receipt = blockchain.create_item(item_data["id"], log_message)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    
  
@blp.route("/view/food-menu/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        log_message = logger.format_log(item_data["name"], Actions.VIEW_FOOD_MENU)
        receipt = blockchain.create_item(item_data["id"], log_message)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}