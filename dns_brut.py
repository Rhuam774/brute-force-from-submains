import requests
from time import sleep
import os

try:
    wordlist = open('wordlist.txt', 'r+')
except Exception as erro:
    print(f'erro: {erro}')   

add_encontrado = open('subdominios_encontrado.txt', 'w')
add_encontrado.close()
a = 0
while True:
    
    site = input("digite o dominio: http's://")
    print('\n=============================================\n')
    for subdomain in wordlist:
        try:
            montagem = 'https://'+site+subdomain
            web = requests.get(montagem)
            if web.status_code == 200:
                add_encontrado = open('subdominios_encontrado.txt', 'a+')
                web.status_code = str(web.status_code)
                add_encontrado.write(montagem+'   '+web.status_code)
                add_encontrado.close()
                os.system('clear')
                print(web.status_code+'\n'+montagem+'\nAdicionado ao arquivo de texto!')
                sleep(3)
                os.system('clear')
            else: 
                print(montagem+'  NÃO CONFIRMADO!\n')
                a += 1
                if a == 100:
                    os.system('clear')
                    a = 0           
        except Exception as erro:
            print(f'erro: {erro}\n')          
            sleep(3)
