import json
import os
import requests
from web3 import Web3
from hexbytes import HexBytes

message_template = "2020-01-01 00:00:00 APP_RU:"
modules = [
    "access",
    "actions",
    "reports",
    "view"
]

class HexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj)
    

# the web3.py method returns an AttributeDict with hexadecimal bytes
# to deserialize it in the response, it must first be encoded
def receipt_deserializer(receipt):
    receipt = dict(receipt)

    for i in range(len(receipt["logs"])):
        receipt["logs"][i] = dict(receipt["logs"][i])
        receipt["logs"][i] = json.dumps(receipt["logs"][i], cls=HexJsonEncoder)
        receipt["logs"][i] = json.loads(receipt["logs"][i])

    receipt = json.dumps(receipt, cls=HexJsonEncoder)
    receipt = json.loads(receipt)
    
    return receipt


def calculate_pad_size():
    highest_count = 0
    for module in modules:
        if len(module) > highest_count:
            highest_count = len(module)
    size = len(message_template) + highest_count
    
    return size


def build_response(transaction_receipt, sent_data):
    base_url = os.getenv("ETHERSCAN_URL")
    etherscan_url = f"{base_url}{transaction_receipt['transactionHash']}"
    response = {
        "sentData": sent_data, 
        "receipt": transaction_receipt, 
        "status": transaction_receipt["status"],
        "etherscanUrl": etherscan_url,
        "transactionPaidPrice": calculate_paid_price(transaction_receipt)
    }

    return response


def calculate_paid_price(transaction_receipt):
    currencies = ["BRL", "USD"]
    gas_price = float(Web3.fromWei(transaction_receipt["effectiveGasPrice"], 'ether'))
    gas_used = transaction_receipt["gasUsed"]
    calculated_prices = {"ETH": gas_price * gas_used}
    try:
        eth_info = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=ETH', timeout=15)
        eth_rates = eth_info.json()["data"]["rates"]

        for currency in currencies:
            currency_rate = float(eth_rates[currency])
            calculated_prices[currency] = currency_rate * gas_price * gas_used
        
    except:
        calculated_prices = {"info": "Timeout error"}

    return calculated_prices

    #https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BRL,USD
