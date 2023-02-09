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