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
    taxa = data["conversion_rate"]
    return taxa
    # print("{:.2f}".format(data["conversion_rate"]))
    
def valorTaxa():
    if select < 1 or select > 9: 
        print('Você deve selecionar um intervalo de 1 a 9!')
    elif select == 1:
        print (valorDaMoeda('USD', 'BRL'))
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
        
def converte_valor(valor):
    if select < 1 or select > 9: 
        print('Você deve selecionar um intervalo de 1 a 9!')
    elif select == 1:
        val_convertido = valor * valorDaMoeda('USD', 'BRL')
        return val_convertido
    elif select == 2:
        val_convertido = valor * valorDaMoeda('BRL','USD')
        return val_convertido
    elif select == 3:
        val_convertido = valor * valorDaMoeda('USD','EUR')
        return val_convertido
    elif select == 4:
        val_convertido = valor * valorDaMoeda('EUR','USD')
        return val_convertido
    elif select == 5:
        val_convertido = valor * valorDaMoeda('EUR', 'BRL')
        return val_convertido
    elif select == 6:
        val_convertido = valor * valorDaMoeda('BRL', 'EUR')
        return val_convertido
    elif select == 7:
        val_convertido = valor * valorDaMoeda('JPY', 'BRL')
        return val_convertido   
    elif select == 8:
        val_convertido = valor * valorDaMoeda('BRL', 'JPY')
        return val_convertido
    else:
        moeda_base = input('Digite a sigla da moeda base: ')
        moeda_destino = input ('Digite a Sigla da moeda destino: ')
        val_convertido = valor * valorDaMoeda(moeda_base, moeda_destino)
        return val_convertido


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

converter_valor_especifico = input('Converter um valor Especifico? (S/N): ')
if converter_valor_especifico != 'S' and converter_valor_especifico != 'N':
    print('Opção selecionada inválida, Digite apenas S ou N')
elif converter_valor_especifico == 'S':
    converter = input('Digite o valor que deseja converter: ')
    valor_a_converter = int(converter)
    print(f'R$ {converte_valor(valor_a_converter)}')
else:
    valorTaxa()


        
        
        
          

        

