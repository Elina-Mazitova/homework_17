import requests


def test_delete_product():
    response = requests.delete(
        "https://fakestoreapi.com/products/1",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    assert response.status_code == 200

def test_delete_product_incorrect_id():
    response = requests.delete(
        "https://fakestoreapi.com/products/1-",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    assert response.status_code == 400