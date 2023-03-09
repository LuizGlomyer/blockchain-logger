from flask.views import MethodView
from flask_smorest import Blueprint, abort
from blockchain.main import blockchain_connection

from utils import utils
from utils.logger import Logger

blp = Blueprint("Reports", "reports", description="Reports of blockchain-stored logs")

logger = Logger("reports")


@blp.route("/reports/<string:user_id>") 
class View(MethodView):
    @blp.response(200)
    def get(cls, user_id):
        
        try:
            WHITESPACE_PAD_SIZE = utils.calculate_pad_size()
            logs = blockchain_connection.fetch_items(user_id)
            
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


@blp.route("/all-reports/<string:user_id>") 
class View(MethodView):
    @blp.response(200)
    def get(cls, user_id):
        WHITESPACE_PAD_SIZE = utils.calculate_pad_size()
        logs = blockchain_connection.fetch_items(user_id)
        
        try:
            reports = {
                "access": [],
                "view": [],
                "actions": []
            }
            print(logs[0], flush=True)
            for i, log in enumerate(logs):
                if log.__contains__('|'):
                    log = log.split(' | ')
                    header = log[0]
                    log[0] = log[0].ljust(WHITESPACE_PAD_SIZE)
                    logs[i] = f"{log[0]} | {log[1]}"
                    if header.__contains__('access'):
                        reports["access"].append(logs[i])
                    elif header.__contains__('view'):
                        reports["view"].append(logs[i])
                    if header.__contains__('actions'):
                        reports["actions"].append(logs[i])
                    
    
            # if some the list becomes unordered because of 
            # unsynchronization due to multiple requests
            

            return {"reports" :reports, "userId": user_id}
        except KeyError:
            abort(404, message="Not found.")
