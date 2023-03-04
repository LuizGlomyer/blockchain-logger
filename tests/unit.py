import pytest
import requests
import urllib.parse
import uuid

base_url = "http://localhost:5000"
#user_id = "email@test.com"
user_id = uuid.uuid4().hex

params = {
  "id": user_id,
  "name": "User"
}


def transact(endpoint):
    print(f"Endpoint - {endpoint}", end="")
    response = requests.post(base_url + endpoint, json=params)
    data = response.json()
    print(f"\tStatus: {data['status']}")
    print(f"Transaction: {data['receipt']['transactionHash']}")

    assert(data["status"] == 1)


@pytest.mark.skip(reason="disabled in favor of testing each endpoint separately")
def test_transaction():
    endpoints = [
      "/access/create-user/",
      "/view/food-menu/",
      "/actions/buy-ticket/"
    ]
  
    print(f"User id: {user_id}")
    error_exists = False
    for i, endpoint in enumerate(endpoints):
      print(f"Endpoint {i + 1} - {endpoint}", end="")
      response = requests.post(base_url + endpoint, json=params)
      data = response.json()
      print(f"\tStatus: {data['status']}")
      if data["status"] != 1:
        error_exists = True
    
    assert(not error_exists)


def test_create_user():
    endpoint = "/access/create-user/"
    transact(endpoint)


def test_view_food_menu():
    endpoint = "/view/food-menu/"
    transact(endpoint)


def test_buy_ticket():
    endpoint = "/actions/buy-ticket/"
    transact(endpoint)


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
