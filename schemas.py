from marshmallow import Schema, fields


class RequestSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()

class BuyTicketSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    amount = fields.Int(required=True)
    price_table_id = fields.Int(required=True)


class ChargeQRCodeSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    charge = fields.Str(required=True)
    registration = fields.Str(required=True)


class ModifyTicketSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    ticket_id = fields.Str(required=True)

class UserByEmailSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    user_email = fields.Str(required=True)

class PriceTableItemSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    meal_id = fields.Str(required=True)
    meal_type = fields.Str(required=True)
    unit_cost = fields.Float(required=True)

class FoodMenuSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    food_menu_id = fields.Str(required=True)
    day_of_week = fields.Str(required=True)
    school_unit = fields.Str(required=True)
    food_type = fields.Str(required=True)
    food_type_description = fields.Str(required=True)

class DeleteFoodMenuSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    food_menu_id = fields.Str(required=True)

class ViewFoodMenuSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    school_unit = fields.Str(required=True)
    day_of_week = fields.Str(required=True)

class CommentSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    observation = fields.Str(required=True)
    rating = fields.Str(required=True)
    price_table_id = fields.Str(required=True)
    comment_id = fields.Str(required=True)

class ViewCommentEmailPriceTableSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    price_table_id = fields.Str(required=True)
