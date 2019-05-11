import names
import requests
import unittest


class TestStringMethods(unittest.TestCase):
    domain = 'http://127.0.0.1:5000'

    def test_add_user(self):
        path_add_user = '/add_user'
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        payload_tuples = [('first_name', first_name),
                          ('last_name', last_name),
                          ('age', '20'),
                          ('sex', 'm'),
                          ('salary', '50000')]
        reponse = requests.post(self.domain + path_add_user, data=payload_tuples)
        print(reponse.json())
        response_add_json = reponse.json()
        self.assertEqual(first_name, response_add_json['first_name'])

#        valid data by read from api
        payload_tuples_login = [('username', first_name),
                          ('password', 'aaaaaa')]
        reponse_login = requests.post(self.domain + '/login', data=payload_tuples_login)
        reponse_login_json=reponse_login.json()
        print(reponse_login_json)
        self.assertEqual(response_add_json['first_name'], reponse_login_json['username'])

if __name__ == '__main__':
    unittest.main()
