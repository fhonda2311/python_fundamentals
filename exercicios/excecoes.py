# -*- coding: utf-8 -*-

# dada a lista

funcionarios = ['joao', 'maria', 'carlos', 'paula', 'mario', 'frodo']

# faça um programa que valide se o usuario é funcionario
# caso seja
# imprima acesso permitido
# caso não
# imprima acesso negado
# sendo que o funcionario frodo está bloqueado
# caso ele tente entrar será exibido um NameError com a seguinte mensagem
# Usuario bloqueado, ir direto pro RH

while True:
    try:
        user = input(f'entre com seu usario: ')
        if user in funcionarios:
            if user == 'frodo':
                raise NameError('Usuario bloqueado, ir direto pro RH')
                break
            else:
                print('acesso permitido')
                break
        else:
            print('acesso negado')
    except NameError as negado:
        print(negado)
    
    
    
    
    #professor
# -*- Coding: utf-8 -*-

# Erros e exceções

# Try/except e finally


# while True:
#     try:
#         x = int(input('Digite o primeiro número: '))
#         y = int(input('Digite o segundo número: '))
#         print(f'Resultado: {x / y}')
#         break
#     except ValueError as v:
#         print(v)
#         print('Digite apenas números!')
#         continue
#     except ZeroDivisionError as z:
#         print(z)
#         print('Número divido por zero')
#         continue
#     finally:
#         print('Calculo de divisão')

# raise exception


funcionarios = ['rafael', 'mariana', 'paulo']



try:
    f = input('Nome: ')
    if f in funcionarios:
        print('você é um funcionario')
    else:
        raise NameError('Você não é funcionario')

except NameError as n:
    print(n)