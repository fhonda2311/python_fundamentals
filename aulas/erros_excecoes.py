# -*- coding: utf-8 -*-

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
