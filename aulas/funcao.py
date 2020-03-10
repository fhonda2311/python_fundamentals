# # # -*- coding: utf-8 -*-


# # # def soma(x,y):
# # #     return x + y

# # # print(soma (10, 21))

# # produtos = []

# # def cadastrar_prod(produto):
# #     global produtos
# #     produtos.append(produto)

# # def listar_prod():
# #     global produtos
# #     for p in produtos:
# #         print(p)

# # cadastrar_prod('teste')
# # cadastrar_prod('teste2')
# # cadastrar_prod('teste3')

# # def deleta_prod(produto):
# #     global produtos
# #     produtos.remove(produto)

# # deleta_prod('teste')

# # listar_prod()


# import requests

# def status_code():
#     SITE = 'https://google.com'
#     return requests.get(SITE)
# print(status_code())


# Lambda

# soma = lambda x,y: x+y
# print(soma(10,20))

numeros = [1,2,3,4,5,6,7,8,9]

dobro = list(map(lambda x: x * 2, numeros))

print(dobro)
