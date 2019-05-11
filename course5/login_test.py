import unittest

import requests


class TestLogin(unittest.TestCase):


    def test_post_login(self):
        response_post_user_json = self.get_login_response()
        print(response_post_user_json)
        self.assertEqual(response_post_user_json['User']['username'], self.username)

    def test_get_current_user(self):
        entry_point = '/api/user'
        headers = {'Content-Type': "application/json",
                   'X-Requested-With': "XMLHttpRequest",
                   'Authorization': "Token " + self.get_login_response()['User']['token'],
                   'cache-control': "no-cache"}
        response = requests.request("GET", self.domain + entry_point, headers=headers).json()
        print(response)
        self.assertEqual(response['User']['username'], self.username)

    def get_login_response(self):
        entry_point = '/api/users/login'
        payload = {"user": {"email": self.email, "password": self.password}}
        headers = {'Content-type': 'application/json'}
        response_post_user_json = \
            requests.post(self.domain + entry_point, json=payload, headers=headers).json()
        return response_post_user_json


if __name__ == '__main__':
    unittest.main()
