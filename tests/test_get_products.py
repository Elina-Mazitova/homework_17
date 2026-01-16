import json
import requests
from jsonschema import validate


def test_get_products():
    response = requests.get("https://fakestoreapi.com/products")
    body = response.json()
    assert response.status_code == 200
    with open("schemas/products_list.json") as file:
        validate(body, schema=json.loads(file.read()))
