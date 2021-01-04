Picqer client python by Jordy van Raalte
==========

This project is a python package to use the Picqer API for python applications. Compatible with Python >= 3.6

The documentation of Picqer can be found on [picqer.com/en/api](https://picqer.com/en/api)

## Installation
```
pip install picqer-client-python
```

## Examples

Installing the package:

```python
from picqer_client_python.picqer_client import Client
```

Creating a Picqer client:
```python
client = Client("--API-KEY--", "https://example.picqer.com/api/v1/")
```
Getting the first 100 orders:
```python
# gets the first 100 orders. Use offset to get more orders
client.orders.get_all()
```

Create a new product
```python
# create new product
product_object = {
    "productcode": "883629-22",
    "name": "Hyperkewl Evaporative Cooling Vest Ultra Blue 7-9yr",
    "price": 54.46
}

# make sure to dump the json.
response = client.products.post(json.dumps(product_object))
print(response.status_code) # 201
```

Process backorders:
```python
# processes backorders
client.backorders.process()
```


## Bug reporting
If you find any bugs in the application please open up an issue in this repository.
