from web3 import Web3
import os
import json

class Connection:
    def __init__(self):
        self.infura_url = f'{os.getenv("PROVIDER_URL")}{os.getenv("API_KEY")}'
        self.web3 = Web3(Web3.HTTPProvider(self.infura_url))
        self.contract_address = f'{os.getenv("CONTRACT_ADDRESS")}'
        
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "contract_abi.json")
        abi = open(path, "r")
        self.contract_abi = json.loads(abi.read())
        self.contract = self.web3.eth.contract(
            address=self.contract_address, abi=self.contract_abi)

        self.from_account = f'{os.getenv("FROM_ACCOUNT")}'
        self.private_key = f'{os.getenv("PRIVATE_KEY")}'

    def fetch_items(self, user_id):
        items = self.contract.functions.retrieveActions(user_id).call({"from":self.from_account})
        return items

    def create_item(self, id, action):
        #TODO tratar falha na transação
        tx = self.contract.functions.store(id, action).build_transaction()
        tx.update({'nonce': self.web3.eth.get_transaction_count(self.from_account)})
        tx['gas'] = self.contract.functions.store(id, action).estimateGas()
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        transaction_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

        #print("transação:")
        #print(tx)
        #print("Transaction hash:", self.web3.toHex(tx_hash))
        #print("Transaction receipt:\n", transaction_receipt)

        return transaction_receipt
    
    def check_tx_by_hash(self, hash):
        return self.web3.eth.get_transaction(hash)

blockchain_connection = Connection()