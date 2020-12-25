Piqcer client python by Jordy van Raalte
==========

This project is python package to use the Piqcer API for python applications. Compatible with Python >= 3.6

The documentation of Piqcer can be found on [picqer.com/en/api](https://picqer.com/en/api)

## Installation
TODO: installation guide

## Examples

Creating a Piqcer client:
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



## Bug reporting
If you find any bugs in the application please open up an issue in this repository.
