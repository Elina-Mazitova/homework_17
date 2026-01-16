import json
import requests
from jsonschema import validate


def test_put_product():
    payload = {
        "title": "Updated Product",
        "price": 11.99,
        "description":"Dog",
        "category" : "Yellow",
        "image" : "http://examples.com"
    }

    response = requests.put(
        "https://fakestoreapi.com/products/1",
        json=payload,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    assert response.status_code == 200

    body = response.json()

    with open("schemas/product_created_or_updated.json") as file:
        schema = json.load(file)

    validate(instance=body, schema=schema)


def test_put_product_incorrect():
    payload = {
        "title": "Updated Product",
        "price": 11.99,
        "description":"Dog",
        "category" : "Yellow",
        "image" : "http://examples.com"
    }

    response = requests.put(
        "https://fakestoreapi.com/products/1-",
        json=payload,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    assert response.status_code == 400

    body = response.json()

    with open("schemas/product_updated_invalid.json") as file:
        schema = json.load(file)

    validate(instance=body, schema=schema)