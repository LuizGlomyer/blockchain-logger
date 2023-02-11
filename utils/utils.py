import json

from hexbytes import HexBytes

class HexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj)
    

# the web3.py method returns an AttributeDict with hexadecimal bytes
# to deserialize it in the response, it must first be encoded
def receipt_deserializer(receipt):
    receipt = dict(receipt)
    receipt = json.dumps(receipt, cls=HexJsonEncoder)
    receipt = json.loads(receipt)
    
    return receipt


def calculate_pad_size():
    modules_list = [
        "access",
        "actions",
        "reports",
        "view"
    ]

    highest_count = 0
    for module in modules_list:
        if len(module) > highest_count:
            highest_count = len(module)
    size = len("2020-01-01 00:00:00 APP_RU:") + highest_count
    
    return size
