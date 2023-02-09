from datetime import datetime
from enum import Enum

class Logger():
    def __init__(self, type):
        self.logger_type = type
        self.app_name = "APP_RU"
    
    def format_log(self, user, action):
        action_description = self.get_action_description(action)
        
        # 2023-12-31 12:00:00   APP:action | User Luiz performed a Pix payment
        log_message = f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} {self.app_name}:{self.logger_type} | User {user} {action_description}"
        return log_message

    def get_action_description(self, action):
        if action == Actions.LOGIN:
            return "logged in"
        elif action == Actions.LOGOFF:
            return "logged off"

        elif action == Actions.VIEW_DATA:
            return "viewed their data"
        elif action == Actions.VIEW_TICKET_LIST:
            return "viewed their ticket list"
        elif action == Actions.VIEW_TICKET_HISTORY:
            return "viewed their ticket history"
        elif action == Actions.VIEW_FOOD_MENU:
            return "viewed the food menu"

        elif action == Actions.BUY_TICKET:
            return "bought a ticket"
        elif action == Actions.SELECT_TICKET:
            return "selected a ticket for consumption"
        elif action == Actions.PIX_PAYMENT:
            return "payed a ticket with Pix"
            
        
class Actions():
    LOGIN = 1
    LOGOFF = 2
    VIEW_DATA = 3
    VIEW_TICKET_LIST = 4
    VIEW_TICKET_HISTORY = 5
    VIEW_FOOD_MENU = 6
    BUY_TICKET = 7
    SELECT_TICKET = 8
    PIX_PAYMENT = 9


