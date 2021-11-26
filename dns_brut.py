import requests
from time import sleep
import os

try:
    wordlist = open('wordlist.txt', 'r')
except Exception as erro:
    print(f'erro: {erro}')   

while True:
    site = input("digite o dominio: http's://")
    print('\n=============================================\n')
    for subdomain in wordlist:
        try:
            montagem = 'https://'+site+subdomain
            web = requests.get(montagem)
            if web.status_code == 200:
                print(web.status_code)
                print(montagem)
                sleep(5)
                try:
                    os.system('clear')
                except:
                    os.system('cls')
        except Exception as erro:
            print(f'erro: {erro}\n')
            sleep(3)
