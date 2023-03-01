import os
from datetime import datetime
from blockchain.main import blockchain_connection
from utils import utils

class Logger():
    def __init__(self, type):
        self.logger_type = type
        self.app_name = os.getenv("APP_NAME")
        self.blockchain_connection = blockchain_connection
        # defines a mininum size for the first part of the log message
        self.WHITESPACE_PAD_SIZE = utils.calculate_pad_size()
    
    def log(self, user, user_interaction):
        formatted_log = self.format_log(user, user_interaction)
        receipt = self.blockchain_connection.create_item(user["id"], formatted_log)
        return receipt
    
    def format_log(self, user, interaction):
        action_description = self.get_interaction_description(interaction)
        
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        name = user.get('name')
        id = user['id']
        first_part = f"{date} {self.app_name}:{self.logger_type}"
        if name and name != "":
            log_message = f"{first_part} | '{name}' [{id}] {action_description}"
        else: 
            log_message = f"{first_part} | [{id}] {action_description}"

        return log_message

    def get_interaction_description(self, interaction):
        if interaction == UserInteractions.LOGIN:
            return "logged in"
        elif interaction == UserInteractions.LOGOFF:
            return "logged off"

        elif interaction == UserInteractions.VIEW_DATA:
            return "viewed their data"
        elif interaction == UserInteractions.VIEW_TICKET_LIST:
            return "viewed their ticket list"
        elif interaction == UserInteractions.VIEW_TICKET_HISTORY:
            return "viewed their ticket history"
        elif interaction == UserInteractions.VIEW_FOOD_MENU:
            return "viewed the food menu"

        elif interaction == UserInteractions.BUY_TICKET:
            return "bought a ticket"
        elif interaction == UserInteractions.SELECT_TICKET:
            return "selected a ticket for consumption"
        elif interaction == UserInteractions.PIX_PAYMENT:
            return "payed a ticket with Pix"
        elif interaction == UserInteractions.CREATE_USER:
            return "created a new user"
            
        
class UserInteractions():
    LOGIN = 1
    LOGOFF = 2
    VIEW_DATA = 3
    VIEW_TICKET_LIST = 4
    VIEW_TICKET_HISTORY = 5
    VIEW_FOOD_MENU = 6
    BUY_TICKET = 7
    SELECT_TICKET = 8
    PIX_PAYMENT = 9
    CREATE_USER = 10
