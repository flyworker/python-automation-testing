import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
reponse = requests.get(url)
print(reponse.json())
print(reponse.json()['bpi']['USD']['rate'])
