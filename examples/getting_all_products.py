from piqcer_client_python.piqcer_client import Client

client = Client("--API-KEY--", "https://example.picqer.com/api/v1/") # --API-KEY-- "--BASE-URL--"


products = []
offset = 0
while True:
    response = client.products.get_all_with_offset(offset)
    for product in response.json():
        products.append(product)

    offset += 100

    if response.json():
        break
