import base64, requests
for i in range(1,100):
    with open(f"Coser-baiyin811-Vol.100-2-MrCong.com-00{str(i)}.jpg", "rb") as image_file:
        b64 = base64.b64encode(image_file.read())

    data = {
                'image': b64,
                'type': 'base64',
            }

    headers = {
        'authorization':'Client-ID 610facfd740080c'
    }

    respone = requests.post('https://api.imgur.com/3/image', headers=headers, data=data).json()
    link = respone['data']['link']
    print(link)
a