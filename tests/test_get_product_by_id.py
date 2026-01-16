import json
import requests
from jsonschema import validate


def test_get_product_by_id():
    response = requests.get("https://fakestoreapi.com/products/1")
    body = response.json()

    assert response.status_code == 200

    with open("schemas/product_by_id.json") as file:
        schema = json.load(file)

    validate(instance=body, schema=schema)
