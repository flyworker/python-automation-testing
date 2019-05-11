import requests
import unittest


class TestStringMethods(unittest.TestCase):
    domain = 'https://maps.googleapis.com'

    def test_distance(self):
        distance = '/maps/api/distancematrix/json?origins=Boston,MA&destinations=Montreal,QC'
        self.reponse = requests.get(self.domain + distance)
        print(self.reponse)
        response_json = self.reponse.json()
        boston_montreal_price = response_json['rows'][0]['elements'][0]['distance']['text']
        self.assertIsInstance(boston_montreal_price, str)
        self.assertEqual('494 km', boston_montreal_price)


if __name__ == '__main__':
    unittest.main()
