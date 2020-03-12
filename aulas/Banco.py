# # -*- coding: utf-8 -*-

# import datetime

# class Conta_bancaria():
    
#     def __init__(self, conta, nome, saldo):
#         self.numeroconta = conta
#         self.nomeusuario = nome
#         self.saldousuario = saldo
#         self.numerobanco = '999'
#         self.numeroagencia = '08'


#     def Deposita(self, valor):
#         self.saldousuario += valor
    
#     def Sacar(self, valor):
#         if self.saldousuario < valor:
#             print('saldo insulficiente')
#         else:
#             self.saldousuario = (self.saldousuario - valor)
#             print(f'valor sacado: {valor}\nSaldo atual: {self.saldousuario}')

#     def Extrato(self):
#         print(f'data da consulta: {datetime.datetime.now()}')
#         print('-'*30)
#         print(f'agencia: {self.numeroagencia} conta: {self.numeroconta}')
#         print(f'saldo em conta: {self.saldousuario}')


# while True:
#     print('banco')
#     print('Bem Vindo!')
#     print("selecione uma opcao!")
#     print("Extrato = 1")
#     print("Saque = 2")
#     print("Deposito = 3")
#     print("Sair = 0")
#     entrada = int(input('>>> '))

#     if entrada == 1:
#         Conta_bancaria.Extrato()
#     elif entrada == 2:
#         Conta_bancaria.Sacar()
#     elif entrada == 3:
#         Conta_bancaria.Deposita()
#     elif entrada == 0:
#         exit()



# conta00001 = Conta_bancaria(9991, 'Fabio Honda', 0)

# # conta00001.Deposita(30000)
# # conta00001.Extrato()

# #prof

# def teste(nome):
#     variavel = nome
#     print(variavel)

# teste('Esse é um teste')
import datetime, time
import os




class Conta_bancaria():
    
    def __init__(self, conta, nome, saldo):
        self.numeroConta = conta
        self.nomeUsuario = nome
        self.saldoUsuario = saldo
        self.numeroBanco = '999'
        self.numeroAgencia = '08'
    
    def deposita(self, valor):
        self.saldoUsuario = (self.saldoUsuario + valor)
    
    def sacar(self, valor):
        if self.saldoUsuario < valor:
            print('Saldo insuficiente')
            time.sleep(2)
            os.system('clear')
        else:
            print(f'Saldo Anterior: R${self.saldoUsuario}')
            self.saldoUsuario = (self.saldoUsuario - valor)
            print(f'Valor sacado: R${valor}\nSaldo Atual: R${self.saldoUsuario}') 
            os.system('clear')

    def extrato(self):
        print(f'Data da consulta: {datetime.datetime.now()}')
        print('-'*20)
        print(f'Cliente: {self.nomeUsuario}')
        print(f'Ag: {self.numeroAgencia} Conta: {self.numeroConta}')
        print(f'Saldo em Conta: R${self.saldoUsuario}')
        time.sleep(3)
        os.system('clear')

conta00001 = Conta_bancaria(9991,'João Amorim',0)

while True:
    print('OldBank')
    print('Bem viindo(a)!')
    print('Selecione a opção abaixo:')
    print('Para extrato digite 1')
    print('Para saque digite 2')
    print('Para deposito digite 3')
    print('Para sair digite 0')
    entrada = int(input('>>> '))
    
    if entrada == 1:
        conta00001.extrato()
    elif entrada == 2:
        sq = int(input('Digite o valor de saque: '))
        conta00001.sacar(sq)
    elif entrada == 3:
        dp = int(input('Digite o valor de deposito: '))
        conta00001.deposita(dp)
    elif entrada == 0:
        exit()
    else:
        print('Valor incorreto')
        continue







