from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_enemys_by_floor():
    floor = 1
    request = client.get("/enemys/" + str(floor))
    assert request.status_code == 200
    assert type(request.json()) == list


def test_enemys_by_floor_random():
    floor = 1
    request = client.get("/enemys/" + str(floor) + "/random")
    assert request.status_code == 200
    assert type(request.json()) == dict


def test_store_route():
    response = client.get("/store")
    assert response.status_code == 200

    data = response.json()
    assert type(data) == list
    assert type(data[0]["items"][0]["name"]) == str


def test_store_route_by_type():
    store_type = "basic"
    response = client.get("/store/" + store_type)
    assert response.status_code == 200

    data = response.json()
    assert type(data) == list
    if data[0]["name"].lower().find(store_type) == -1:
        assert False
    assert True
