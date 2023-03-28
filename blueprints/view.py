from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import RequestSchema, ChargeQRCodeSchema, UserByEmailSchema, ViewFoodMenuSchema, ViewCommentEmailPriceTableSchema, HistorySchema
from blockchain.main import Connection

from utils.utils import receipt_deserializer, build_response
from utils.logger import Logger, UserInteractions

blp = Blueprint("View", "view", description="Visualizing system data")
blockchain = Connection()
logger = Logger("view")


@blp.route("/view/data/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_DATA)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/view/ticket-list/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_TICKET_LIST)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/view/ticket-history/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_TICKET_HISTORY)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    
  
@blp.route("/view/food-menu/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_FOOD_MENU)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/view/ticket-not-consumed/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_TICKET_NOT_CONSUMED)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/view/first-ticket-not-consumed/")
class View(MethodView):
    @blp.arguments(ViewCommentEmailPriceTableSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_FIRST_TICKET_NOT_CONSUMED)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/view/comment/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_COMMENT)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/view/comment-email-price-table/")
class View(MethodView):
    @blp.arguments(ViewCommentEmailPriceTableSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_COMMENT_EMAIL_PRICE_TABLE)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/view/price-table/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_PRICE_TABLE)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/view/user/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_USER)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/view/user-by-email/")
class View(MethodView):
    @blp.arguments(UserByEmailSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_USER_BY_EMAIL)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/view/food-menu-by-day-school/")
class View(MethodView):
    @blp.arguments(ViewFoodMenuSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_FOOD_MENU_BY_DAY_SCHOOL)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/view/history/")
class View(MethodView):
    @blp.arguments(HistorySchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_HISTORY)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
