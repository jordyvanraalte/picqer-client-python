from piqcer_client.piqcer_client import Client
import json

client = Client("--API-KEY--", "https://example.picqer.com/api/v1/")

# gets the first 100 orders. Use offset to get more orders
client.orders.get_all()

#create new products
product_object = {
    "productcode": "883629-22",
    "name": "Hyperkewl Evaporative Cooling Vest Ultra Blue 7-9yr",
    "price": 54.46
}

# make sure to dump the json.
response = client.products.post(json.dumps(product_object))
print(response.status_code) # 201

# processes backorders
client.backorders.process()
