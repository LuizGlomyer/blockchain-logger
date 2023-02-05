from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Int(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)

class AccessSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    #teste = fields.Str(required=True)