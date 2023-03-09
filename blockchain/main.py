from web3 import Web3
import os
import time
import json
from statistics import median
from threading import Semaphore

class Connection:
    def __init__(self):
        self.semaphore = Semaphore()
        self.infura_url = f'{os.getenv("PROVIDER_URL")}{os.getenv("INFURA_API_KEY")}'
        self.web3 = Web3(Web3.HTTPProvider(self.infura_url))
        self.contract_address = f'{os.getenv("CONTRACT_ADDRESS")}'
        
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "contract_abi.json")
        abi = open(path, "r")
        self.contract_abi = json.loads(abi.read())
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

        self.from_account = f'{os.getenv("FROM_ACCOUNT")}'
        self.private_key = f'{os.getenv("PRIVATE_KEY")}'
    
    def is_transacting(self):
        return self.semaphore._value == 0


    def fetch_items(self, user_id):
        items = self.contract.functions.retrieveInteractions(user_id).call({"from":self.from_account})
        return items


    def create_item(self, mapping_id, log_message):
        while self.is_transacting():
            time.sleep(0.25)

        if not self.is_transacting():
            self.semaphore.acquire()

            def estimate_chain_gas():
                last_block = self.web3.eth.get_block("latest", full_transactions=True)
                transactions = last_block.transactions
                # Returns the median of the gas in previous block transactions
                return int(median(t.gas for t in transactions)) 
            #print(estimate_chain_gas(), flush=True) 
            
            tx = self.contract.functions.logMessage(mapping_id, log_message).build_transaction()
            tx.update({'nonce': self.web3.eth.get_transaction_count(self.from_account)})
            tx['gas'] = self.contract.functions.logMessage(mapping_id, log_message).estimateGas()
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            transaction_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            self.semaphore.release()
            return transaction_receipt
    

    def check_tx_by_hash(self, hash):
        return self.web3.eth.get_transaction(hash)

blockchain_connection = Connection()
