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
    
    def log(self, user_data, user_interaction):
        formatted_log = self.format_log(user_data, user_interaction)
        receipt = self.blockchain_connection.create_item(user_data["id"], formatted_log)
        return receipt
    
    def format_log(self, user_data, interaction):
        action_description = self.get_interaction_description(interaction, user_data)
        
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        name = user_data.get('name')
        id = user_data['id']
        first_part = f"{date} {self.app_name}:{self.logger_type}"
        if name and name != "":
            log_message = f"{first_part} | '{name}' [{id}] {action_description}"
        else: 
            log_message = f"{first_part} | [{id}] {action_description}"

        return log_message

    def get_interaction_description(self, interaction, user_data):
        data = user_data.copy()
        data.pop("id"); data.pop("name")

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
            if user_data["amount"] > 1:
                quantity = f"{user_data['amount']} tickets"
            else:
                quantity = f"{user_data['amount']} ticket"
            return f"bought {quantity} of item {user_data['price_table_id']}"
        
        elif interaction == UserInteractions.SELECT_TICKET:
            return "selected a ticket for consumption"
        
        elif interaction == UserInteractions.PIX_PAYMENT:
            return "payed a ticket with Pix"
        
        elif interaction == UserInteractions.CREATE_USER:
            return "created a new user"


        elif interaction == UserInteractions.VIEW_USER:
            return f"viewed the user informations"
        
        elif interaction == UserInteractions.VIEW_USER_BY_EMAIL:
            return f"viewed user information for following e-mail: {user_data['user_email']}"
        
        elif interaction == UserInteractions.CREATE_PRICE_TABLE_ITEM:
            return f"created a new item in the price table: {data}"
        
        elif interaction == UserInteractions.VIEW_PRICE_TABLE:
            return f"viewed the price table"    
        
        elif interaction == UserInteractions.EDIT_PRICE_TABLE:
            return f"edited the price table: {data}"
        
        elif interaction == UserInteractions.DELETE_ITEM_PRICE_TABLE:
            return f"deleted from the price table: {user_data['meal_id']}"
        
        elif interaction == UserInteractions.CREATE_DAY_FOOD_MENU:
            return f"created a new food menu: {data}"
        
        elif interaction == UserInteractions.VIEW_FOOD_MENU:
            return f"viewed the food menu"
        
        elif interaction == UserInteractions.VIEW_FOOD_MENU_BY_DAY_SCHOOL:
            return f"viewed the food menu of {user_data['day_of_week']} of {user_data['school_unit']}"
        
        elif interaction == UserInteractions.EDIT_FOOD_MENU:
            return f"edited the food menu: {data}"
        
        elif interaction == UserInteractions.DELETE_ITEM_FOOD_MENU:
            return f"deleted an item from food menu: \"{user_data['food_menu_id']}\""
        
        elif interaction == UserInteractions.VIEW_HISTORY:
            return f"viewed their history from {user_data['start_date']} to {user_data['end_date']}"
        
        elif interaction == UserInteractions.CREATE_COMMENT:
            return f"created a new comment: {data}"
        
        elif interaction == UserInteractions.VIEW_COMMENT:
            return f"viewed the comments"
        
        elif interaction == UserInteractions.VIEW_COMMENT_EMAIL_PRICE_TABLE:
            return f"viewed the comments of {user_data['price_table_id']}"
        
        elif interaction == UserInteractions.VIEW_TICKET_BY_EMAIL:
            return f"viewed the tickets by e-mail"
        
        elif interaction == UserInteractions.VIEW_TICKET_NOT_CONSUMED:
            return f"viewed tickets not consumed"
        
        elif interaction == UserInteractions.VIEW_FIRST_TICKET_NOT_CONSUMED:
            return f"viewed tickets not consumed of item {user_data['price_table_id']}"
        
        elif interaction == UserInteractions.VIEW_CHARGE_QR_CODE:
            return f"charged the QR Code with {user_data['charge']}, registration: {user_data['registration']}"
        
        elif interaction == UserInteractions.EDIT_TICKET:
            return f"edited the ticket: {user_data['ticket_id']} of item {user_data['price_table_id']}"
        
        elif interaction == UserInteractions.CONSUME_TICKET:
            return f"consumed the ticket: {user_data['ticket_id']}"

        
class UserInteractions():
    LOGIN = 1
    LOGOFF = 2
    VIEW_DATA = 3
    VIEW_TICKET_LIST = 4
    VIEW_TICKET_HISTORY = 5
    SELECT_TICKET = 8
    PIX_PAYMENT = 9
    
    CREATE_USER = 10
    VIEW_USER = 11
    VIEW_USER_BY_EMAIL = 12

    CREATE_PRICE_TABLE_ITEM = 13
    VIEW_PRICE_TABLE = 14
    EDIT_PRICE_TABLE = 15
    DELETE_ITEM_PRICE_TABLE = 16

    CREATE_DAY_FOOD_MENU = 17
    VIEW_FOOD_MENU = 6
    VIEW_FOOD_MENU_BY_DAY_SCHOOL = 18
    EDIT_FOOD_MENU = 19
    DELETE_ITEM_FOOD_MENU = 20

    VIEW_HISTORY = 21

    CREATE_COMMENT = 22
    VIEW_COMMENT = 23
    VIEW_COMMENT_EMAIL_PRICE_TABLE = 24

    BUY_TICKET = 7
    VIEW_TICKET_BY_EMAIL = 25
    VIEW_TICKET_NOT_CONSUMED = 26
    VIEW_FIRST_TICKET_NOT_CONSUMED = 27
    VIEW_CHARGE_QR_CODE = 28
    EDIT_TICKET = 29
    CONSUME_TICKET = 30
