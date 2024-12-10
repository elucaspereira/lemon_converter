# neste primeiro momento vou criar um conversor simples e conforme for aprendendo mais aprimoro o sistema 
# 1° funcionalidade: conversor de  peso e massa
#Gramas (g) → Quilogramas (kg) → Toneladas (t) → Libras (lb) → Onças (oz)

print('-'*50)
print('Bem vindo ao conversor de unidade')
print(
    'Grama para Quilos    (1) \n' 
    'Quilos para Gramas   (2) \n'
    'Quilos para Tonelada (3) \n'
    'Tonelada para Quilos (4) \n'
)
print('-'*50)

def grama_para_quilo(grama):
        return grama / 1000

def quilos_para_grama(quilos):
        return quilos * 1000

def quilos_para_toneladas(quilos):
        return quilos / 1000

def tonelada_para_quilos(tonelada):
        return tonelada * 1000


escolha = int(input('Selecione a opção de conversão que deseja realizar: '))

if escolha < 1 or escolha > 4:
        print('[ERRO: Verifique a opção digitada e tente novamente]')

elif escolha == 1:
        print('[Selecionado a conversão de Grama(g) para Quilos(KG)]')
        valor_inserido = input('Digite o valor que deseja converter: ')
        grama = float(valor_inserido)
        result = grama_para_quilo(grama)
        print(f'O valor convertido é: {result:.3f} KG')
elif escolha == 2:
        print('[Selecionado a conversão de Quilos(KG) para Gramas(g)]')
        valor_inserido = input('Digite o valor que deseja converter: ')
        quilos = float(valor_inserido)
        result = quilos_para_grama(quilos)
        print(f'O valor convertido é: {result:.3f} g')
elif escolha == 3:
        print('[Selecionado a conversão de Quilos(KG) para Tonelada(t)]')
        valor_inserido = input('Digite o valor que deseja converter: ')
        quilos = float(valor_inserido)
        result = quilos_para_toneladas(quilos)
        print(f'O valor convertido é: {result:.3f} t')
else:
        print('[Selecionado a conversão de Tonelada(t) para Quilos(KG)]')
        valor_inserido = input('Digite o valor que deseja converter: ')
        tonelada = float(valor_inserido)
        result = quilos_para_toneladas(tonelada)
        print(f'O valor convertido é: {result:.3f} kg')
        
        



        