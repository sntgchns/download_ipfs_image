import requests

image_url = 'https://ipfs.io/ipfs/QmarkkgfaHJH1RgaXneeayrw7ygKkKoHzchUYkFatxY5jY'

img_data = requests.get(image_url).content
with open(image_url.split('/')[-1]+'.png', 'wb') as handler:
    handler.write(img_data)