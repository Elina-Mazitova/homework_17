import json
import requests
from jsonschema import validate


def test_post_product():
    payload = {
        "title": "New Product",
        "price": 29.99,
        "description":"Cat",
        "category" : "Red",
        "image" : "http://example.com"
    }

    response = requests.post(
        "https://fakestoreapi.com/products",
        json=payload,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    assert response.status_code == 201

    body = response.json()

    with open("schemas/product_created_or_updated.json") as file:
        schema = json.load(file)

    validate(instance=body, schema=schema)
