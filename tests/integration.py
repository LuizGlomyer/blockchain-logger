import requests
import urllib.parse
import uuid

base_url = "http://localhost:8080"
#user_id = "email@test.com"
user_id = uuid.uuid4().hex

user_params = {
  "id": "lcgpgj.snf20@uea.edu.br",
  "name": "User"
}


def transact(endpoint, params):
    params |= user_params
    print(params)
    print(f"Endpoint - {endpoint}", end="")
    response = requests.post(base_url + endpoint, json=params)
    
    data = response.json()
    data = data['receipt']
    print(f"\tStatus: {data['status']}")
    print(f"Transaction: {data['receipt']['transactionHash']}")

    assert(data["status"] == 1)


def test_create_user():
    params = {"institutionalEmail": user_params["id"]}
    endpoint = "/user/"
    transact(endpoint, params)


def test_view_food_menu():
    params = {}
    endpoint = "/food-menu/"
    
    print(params)
    print(f"Endpoint - {endpoint}", end="")
    response = requests.get(base_url + endpoint)
    
    data = response.json()
    data = data['receipt']
    print(f"\tStatus: {data['status']}")
    print(f"Transaction: {data['receipt']['transactionHash']}")

    assert(data["status"] == 1)


def test_buy_ticket():
    params = {"amount": 3, "priceTableId": "555", "userEmail": user_params["id"], "consumed": True}
    endpoint = "/ticket/"
    transact(endpoint, params)


def test_reports():
    encoded_id = urllib.parse.quote(user_id)
    params = {
      "user_id": user_id
    }

    response = requests.get("http://localhost:5000" + "/reports/" + encoded_id, params=params)
    data = response.json()
    for interaction in data["logs"]:
       print(interaction)

    assert(data["id"] == user_id)
    assert(type(data["logs"]) == list)
