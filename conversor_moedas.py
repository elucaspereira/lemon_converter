from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('API_KEY')

print('carregando variaveis')

if api_key:
    print('Chave de API recuperada com sucesso!')
else:
    print('Chave de API não definida!')



# import requests

# url = 'https://v6.exchangerate-api.com/v6/593879fb59936939ae1e035e/latest/USD'

# response = requests.get(url)
# data = response.json()

# print(data)