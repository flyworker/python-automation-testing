import requests
import unittest



class TestStringMethods(unittest.TestCase):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    reponse = requests.get(url)

    
    def test_btc_price(self):
        btc_json = self.reponse.json()
        btc_price = btc_json['bpi']['USD']['rate']
        self.assertIsInstance(btc_price,str)
        btc_price_float=float(str(btc_price).replace(",", ""))
        print(btc_price_float)
        
        rate_float=  btc_json['bpi']['USD']['rate_float']
        self.assertEqual( btc_price_float,rate_float)


    def test_btc_GPDprice(self):
        btc_json = self.reponse.json()
        btc_price = btc_json['bpi']['GBP']['rate']
        self.assertIsInstance(btc_price,str)

if __name__ == '__main__':
      unittest.main()