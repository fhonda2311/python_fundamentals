# -*- coding: utf-8 -*-

class servidor():
    def __init__(self):
        self.cpu = None
        self.memoria = None
        self.disco = None

dns = servidor()

dns.cpu = 'intel  xeon'

print(dns.cpu)