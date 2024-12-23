from dotenv import load_dotenv
import os

import requests

load_dotenv()


api_key = os.getenv('API_KEY') #RECUPERA A CHAVE DA API

#funcao que calcula o valor da taxa da moeda que deseja converter
def valorDaMoeda(moedaBase, moedaDestino):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{moedaBase}/{moedaDestino}'
    response = requests.get(url)
    data = response.json()
    print("{:.2f}".format(data["conversion_rate"]))


if api_key:
    print('Chave de API recuperada com sucesso!')
else:
    print('Chave de API não definida!')



import requests
select_type_conversion = input( #RECEBE O TIPO DE CONVERSAO QUE O USUARIO DESEJA PARA QUE RETORNE A TAXA NA FUNCAO  VALOR DA MOEDA
               'selecione a conversão que deseja realizar: \n'
               '[1]: Dolar dos Estados Unidos para Real \n'
               '[2]: Real para Dolar dos Estados Unidos \n'
               '[3]: Dolar dos Estados Unidos para Euro \n'
               '[4]: Euro para Dolar dos Estados Unidos \n'
               '[5]: Euro para Real \n'
               '[6]: Real para Euro \n'
               '[7]: Iene Japones para Real \n'
               '[8]: Real para Iene Japones \n'
               '[9]: Selecione manualmente a Moeda base e a moeda de destino conforme exemplo: (EUR , USD) \n'
               'Digite uma das opções: '
               )
select = int(select_type_conversion)
print('Carregando Dados...')

if select < 1 or select > 9: 
    print('Você deve selecionar um intervalo de 1 a 9!')
elif select == 1:
    valorDaMoeda('USD', 'BRL')
elif select == 2:
    valorDaMoeda('BRL','USD')
elif select == 3:
    valorDaMoeda('USD','EUR')
elif select == 4:
    valorDaMoeda('EUR','USD')
elif select == 5:
    valorDaMoeda('EUR', 'BRL')
elif select == 6:
     valorDaMoeda('BRL', 'EUR')
elif select == 7:
     valorDaMoeda('JPY', 'BRL')   
elif select == 8:
     valorDaMoeda('BRL', 'JPY')
else:
    moeda_base = input('Digite a sigla da moeda base: ')
    moeda_destino = input ('Digite a Sigla da moeda destino: ')
    valorDaMoeda(moeda_base, moeda_destino)