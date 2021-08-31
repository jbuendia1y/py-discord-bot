from fastapi.testclient import TestClient
from app import app

from test.helpers import reset_players, reset_db_for_testing, players_for_test

client = TestClient(app)


def test_enemys_by_floor():
    reset_db_for_testing()
    floor = 1
    request = client.get("/enemys/" + str(floor))
    assert request.status_code == 200
    assert type(request.json()) == list


def test_enemys_by_floor_random():
    reset_db_for_testing()
    floor = 1
    request = client.get("/enemys/" + str(floor) + "/random")
    assert request.status_code == 200
    assert type(request.json()) == dict


def test_store_route():
    reset_db_for_testing()
    response = client.get("/store")
    assert response.status_code == 200

    data = response.json()
    assert type(data) == list
    assert type(data[0]["items"][0]["name"]) == str


def test_store_route_by_type():
    reset_db_for_testing()
    store_type = "basic"
    response = client.get("/store/" + store_type)
    assert response.status_code == 200

    data = response.json()
    assert type(data) == list
    if data[0]["name"].lower().find(store_type) == -1:
        assert False
    assert True


def test_hunt_route():
    reset_players()
    response = client.post("/battles/hunt?id=" + players_for_test[0]["id"])
    assert response.status_code == 200
    assert type(response.json()["id"]) == str
