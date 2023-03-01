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
        from utils import utils
        try:
            WHITESPACE_PAD_SIZE = utils.calculate_pad_size()
            print(WHITESPACE_PAD_SIZE, flush=True)
            logs = blockchain_connection.fetch_items(user_id)   
            print(logs, flush=True)
            for i, log in enumerate(logs):
                if log.__contains__('|'):
                    log = log.split(' | ')
                    log[0] = log[0].ljust(WHITESPACE_PAD_SIZE)
                    logs[i] = f"{log[0]} | {log[1]}"
    
            # if some the list becomes unordered because of 
            # unsynchronization due to multiple requests
            logs.sort()
    
            return {"logs": logs, "id": user_id}
        except KeyError:
            abort(404, message="Not found.")
