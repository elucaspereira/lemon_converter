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
    taxa = float(data["conversion_rate"]) #converte a taxa para float
    return taxa
    
    
def valorTaxa(select): #recupera o valor da taxa do dia de acordo com a moeda selecionada
    if select < 1 or select > 9: 
        print('Você deve selecionar um intervalo de 1 a 9!')
    elif select == 1:
        print(f'O valor da taxa é de R$: {valorDaMoeda("USD", "BRL"):.2f}')
    elif select == 2:
        print(f'O valor da Taxa é de $:  {valorDaMoeda("BRL","USD"):.2f}')  
    elif select == 3:
        print(f'O valor da Taxa é de €:  {valorDaMoeda("USD","EUR"):.2f}')
    elif select == 4:
        print(f'O valor da Taxa é de $:  {valorDaMoeda("EUR","USD"):.2f}')
    elif select == 5:
        print(f'O valor da Taxa é de R$:  {valorDaMoeda("EUR", "BRL"):.2f}')
    elif select == 6:
        print(f'O valor da Taxa é de €:  {valorDaMoeda("BRL", "EUR"):.2f}')
    elif select == 7:
        print(f'O valor da Taxa é de R$:  {valorDaMoeda("JPY", "BRL"):.2f}')   
    elif select == 8:
        print(f'O valor da Taxa é de ¥:  {valorDaMoeda("BRL", "JPY"):.2f}')
    else:
        moeda_base = input('Digite a sigla da moeda base: ')
        moeda_destino = input ('Digite a Sigla da moeda destino: ')
        print(valorDaMoeda(moeda_base, moeda_destino))
        
def converte_valor(valor,select): #converte um valor especifico informado pelo usuario
    if select < 1 or select > 9: 
        print('Você deve selecionar um intervalo de 1 a 9!')
    elif select == 1:
        taxa = valorDaMoeda('USD', 'BRL')
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')
        
    elif select == 2:
        taxa = valorDaMoeda('BRL','USD')
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')
    elif select == 3:
        taxa = valorDaMoeda('USD','EUR')
        val_convertido = valor * taxa 
        print(f'Valor convertido: R$ {val_convertido:.2f}')
    elif select == 4:
        taxa = valorDaMoeda('EUR','USD')
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')
    elif select == 5:
        taxa = valorDaMoeda('EUR', 'BRL')
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')
    elif select == 6:
        taxa = valorDaMoeda('BRL', 'EUR')
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')
    elif select == 7:
        taxa = valorDaMoeda('JPY', 'BRL')
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')  
    elif select == 8:
        taxa = valorDaMoeda('BRL', 'JPY')
        val_convertido = valor * taxa
        print(f'Valor convertido: ¥ {val_convertido:.2f}')
    else:
        moeda_base = input('Digite a sigla da moeda base: ')
        moeda_destino = input ('Digite a Sigla da moeda destino: ')
        taxa = valorDaMoeda(moeda_base, moeda_destino)
        val_convertido = valor * taxa
        print(f'Valor convertido: R$ {val_convertido:.2f}')


if api_key:
    print('Chave de API recuperada com sucesso!')
else:
    print('Chave de API não definida!')




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

converter_valor_especifico = input('Converter um valor Especifico? (S/N): ').upper()
if converter_valor_especifico != 'S' and converter_valor_especifico != 'N':
    print('Opção selecionada inválida, Digite apenas S ou N')
elif converter_valor_especifico == 'S':
    converter = input('Digite o valor que deseja converter: ')
    valor_a_converter = float(converter)
    converte_valor(valor_a_converter,select)
else:
    valorTaxa(select)