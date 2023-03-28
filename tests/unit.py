import requests
import urllib.parse
import uuid

base_url = "http://localhost:5000"
#user_id = "email@test.com"
user_id = uuid.uuid4().hex
user_id = "glomyer@uea.edu.br"

user_params = {
  "id": user_id,
  "name": "User"
}


def transact(endpoint, params):
    params |= user_params
    print(params)
    print(f"Endpoint - {endpoint}", end="")
    response = requests.post(base_url + endpoint, json=params)
    data = response.json()
    print(f"\tStatus: {data['status']}")
    print(f"Transaction: {data['receipt']['transactionHash']}")

    assert(data["status"] == 1)


def test_create_user():
    params = {}
    endpoint = "/access/create-user/"
    transact(endpoint, params)


def test_view_food_menu():
    params = {}
    endpoint = "/view/food-menu/"
    transact(endpoint, params)


def test_buy_ticket():
    params = {"amount": 3, "price_table_id": "555"}
    endpoint = "/actions/buy-ticket/"
    transact(endpoint, params)


def test_reports():
    encoded_id = urllib.parse.quote(user_id)
    params = {
      "user_id": user_id
    }

    response = requests.get(base_url + "/reports/" + encoded_id, params=params)
    data = response.json()
    for interaction in data["logs"]:
       print(interaction)

    assert(data["id"] == user_id)
    assert(type(data["logs"]) == list)

