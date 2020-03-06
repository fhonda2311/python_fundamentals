#Dados a lista

#times = ['time',['Brasil', 'Japao','Argentina','Italia'], 'cores', ['Amarelo','Vermelho','Azul','Verde']]

#print(f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][2]}, {times[3][3]}')

1.
# dado a lista

#times = ['time', ['Corinthians', 'Palmeiras', 'São Paulo'], 'cores', ['Preto', 'Branco', 'Verde', 'Vermelho']]

# imprima na tela as seguintes mensagens:


# time: <nome_time>, cores: <cores_time>

#print(f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][1]}')
#print(f'{times[0]}: {times[1][1]}, {times[2]}: {times[3][2]}, {times[3][1]}')
#print(f'{times[0]}: {times[1][2]}, {times[2]}: {times[3][0]}, {times[3][1]}, {times[3][33]}')


2. 

# dado o dicionario:

dados = {
    'estados': {
        'sp':{
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg':{
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }

}

# Imprima as seguintes informações:

# 1. Nome dos estados

# 2. Nome dos estados, quantidade de municipios e  população


# print(dados['estados']['sp']['nome'])


# Calculo de notas
# peça 4 notas do aluno
# se a nota final for maior que 7
# imprima aprovado
# se não
#imprima reprovado

# Crie um script em python que receba dois números e que informe ao usuário qual deles é maior.

# n1 = float(input('Entre com a nota 1:'))
# n2 = float(input('Entre com a nota 2:'))
# n3 = float(input('Entre com a nota 3:'))
# n4 = float(input('Entre com a nota 4:'))

# m = (n1+n2+n3+n4)/4
# if m >= 7:
#     print(f'aprovado')
#     print (f'Sua media eh = {m}')
# else:
#     print(f'reprovado')
#     print (f'Sua media eh = {m}')


n1 = int(input('Entre com a numero 1:'))
n2 = int(input('Entre com a numero 2:'))

if n1 = n2:
    print('n1 sao iguais n2')
else:
    if n1 > n2:
        print('n1 eh maior que n2')
    else:
        print('n2 maior que n1')
