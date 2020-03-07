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
    
