

import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import AccessSchema
from blockchain.main import Connection

blp = Blueprint("Access", "access", description="Login e logout do sistema")
blockchain = Connection()

@blp.route("/access/<string:user_id>") 
class Access(MethodView):
    @blp.response(200)
    def get(cls, user_id):
        try:
            print(blockchain.fetch_items(), flush=True)
            print(user_id, flush=True)
            return {"id":user_id, "name": "nome", "teste":1}
        except KeyError:
            abort(404, message="Store not found.")
    
@blp.route("/access/")
class Access(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        blockchain.create_item(int(item_data["id"]))
        print(item_data, flush=True)
        
        return item_data