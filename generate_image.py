import requests
import json
import base64
from secrets_keys import SECRET_KEY, API_KEY


def generate_image(request: str):
    class Text2ImageAPI:
        def __init__(self, url, api_key, secret_key):
            self.URL = url
            self.AUTH_HEADERS = {
                'X-Key': f'Key {api_key}',
                'X-Secret': f'Secret {secret_key}',
            }

        def get_model(self):
            response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
            data = response.json()
            return data[0]['id']

        def generate(self, prompt, model, images=1, width=600, height=400):
            params = {
                "type": "GENERATE",
                "numImages": images,
                "width": width,
                "height": height,
                "generateParams": {
                    "query": f"{prompt}"
                }
            }

            data = {
                'model_id': (None, model),
                'params': (None, json.dumps(params), 'application/json')
            }
            response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
            data = response.json()
            return data['uuid']

        def check_generation(self, request_id, attempts=60):
            while attempts > 0:
                response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
                data = response.json()
                if data['status'] == 'DONE':
                    return data['images']

                attempts -= 1

    def gen(prom):
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
        model_id = api.get_model()
        uuid = api.generate(prom, model_id)
        print([uuid])
        images = api.check_generation(uuid)

        # Здесь image_base64 - это строка с данными изображения в формате base64
        image_base64 = images[0]

        # Декодируем строку base64 в бинарные данные
        image_data = base64.b64decode(image_base64)

        # Открываем файл для записи бинарных данных изображения
        try:
            with open(f"image.jpg", "wb") as file:
                file.write(image_data)
        except:
            with open(f"image.jpg", "w+") as file:
                file.write(image_data)

    gen(request.replace("\n", " "))
