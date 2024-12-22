from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('API_KEY')

print('carregando variaveis')

if api_key:
    print('Chave de API recuperada com sucesso!')
else:
    print('Chave de API não definida!')



import requests
select_type_conversion = input(
               '[1]: Dolar para Real \n'
               '[2]: Real para Dolar \n'
               'selecione a conversão que deseja realizar: '
               )
select = int(select_type_conversion)
print('Carregando Dados...')

if select == 1:
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/BRL'
    response = requests.get(url)
    data = response.json()
    print(data["conversion_rate"])
else:
    print('erro')