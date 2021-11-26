import requests

while True:
    web = requests.get('https://google.com')
    print(web.status_code)

