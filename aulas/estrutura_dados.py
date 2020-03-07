# -*- coding: utf-8 -*-

# listas

#Frutas = ['pera', 'maca', 'uva', 'melancia']

#print(Frutas[0])

#lista = [2, 1.4, 'cachorro', False, ['s', 'd', 'r', 'j']]

# Tupla


imutaveis = (1, 2, 3, ['a','b','c'], 'limao')

# -*- coding: utf-8 -*-

# listas

frutas = ['abacaxi', 'maçã', 'limão']

lista = [1, 1.5, 'passarro', False, ['a', 'b', 'c'], frutas]

# Fatiamento de listas
# print(frutas)
# print(frutas[1]) # indexação em listas
    lista[2] = 'cachoro'
# print(lista[4][1])
# print(lista)

# Métodos de lista

# lista.append('cavalo')
# print(lista.count('passaro'))
# print(lista.index('passaro'))
# print(lista.remove('cavalo'))
# lista.pop(0)

# print(len(lista))
# lista.insert(0, 'abacaxi')
# print(lista)


# tuplas

# imutaveis = (1, 2, 3, ['a','b','c'], 'limão')
# # print(type(imutaveis))
# print(imutaveis.count('limao'))
# print(imutaveis.index(3))
# print(imutaveis[3][1])

# Dicionarios

# dicionario = {'nome': 'Renato', 'sobrenome': 'Barbosa', 'idade' .26}

# dicionario['idade'] = 27
# print(dicionario['idade'])
# print(dicionario.keys())
# print(dicionario.values())
# dicionario.pop('idade')
# print(dicionario.items())


produtos = {'produtos': {'OOO1': {'nome': 'camiseta hulk',
                                  'valor': 79.9},
                         '0002': {'nome': 'camiseta star wars',
                                  'valor': 99.9}
                         }
            }

print(produtos['produtos']['0001'].values())
print(produtos['produtos']['0001'].keys())
print(produtos['produtos']['0001']['nome'])
















