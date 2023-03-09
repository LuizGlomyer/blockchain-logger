from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import RequestSchema, BuyTicketSchema, ModifyTicketSchema, PriceTableItemSchema, FoodMenuSchema, DeleteFoodMenuSchema, CommentSchema


from utils.utils import receipt_deserializer, build_response
from utils.logger import Logger, UserInteractions

blp = Blueprint("Actions", "actions", description="User-made actions on the system")
logger = Logger("actions")


@blp.route("/actions/buy-ticket/")
class View(MethodView):
    @blp.arguments(BuyTicketSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.BUY_TICKET)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/select-ticket/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.SELECT_TICKET)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
    

@blp.route("/actions/pix-payment/")
class View(MethodView):
    @blp.arguments(RequestSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.PIX_PAYMENT)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/create-price-table-item/")
class View(MethodView):
    @blp.arguments(PriceTableItemSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.CREATE_PRICE_TABLE_ITEM)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/edit-price-table/")
class View(MethodView):
    @blp.arguments(PriceTableItemSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.EDIT_PRICE_TABLE)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/delete-price-table-item/")
class View(MethodView):
    @blp.arguments(PriceTableItemSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.DELETE_ITEM_PRICE_TABLE)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/create-day-food-menu/")
class View(MethodView):
    @blp.arguments(FoodMenuSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.CREATE_DAY_FOOD_MENU)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/edit-food-menu/")
class View(MethodView):
    @blp.arguments(FoodMenuSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.EDIT_FOOD_MENU)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/delete-item-food-menu/")
class View(MethodView):
    @blp.arguments(DeleteFoodMenuSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.DELETE_ITEM_FOOD_MENU)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/create-comment/")
class View(MethodView):
    @blp.arguments(CommentSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.CREATE_COMMENT)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/edit-ticket/")
class View(MethodView):
    @blp.arguments(ModifyTicketSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.EDIT_TICKET)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)


@blp.route("/actions/consume-ticket/")
class View(MethodView):
    @blp.arguments(ModifyTicketSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.CONSUME_TICKET)
        deserialized_receipt = receipt_deserializer(receipt)
        return build_response(deserialized_receipt, item_data)
