import unittest

import requests


class TestStringMethods(unittest.TestCase):
    domain = 'https://postman-echo.com'

    def test_get_user(self):
        entry_point = '/get'

        payload = {'user': 'jim'}
        response_get_user_json = requests.get(self.domain + entry_point, params=payload).json()
        print(response_get_user_json)
        self.assertEqual(response_get_user_json['args']['user'], 'jim')

    def test_post_stange(self):
        enter_point='/post'
        payload = {'strange': 'boom'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # data = {"a": 1, "b": 2}
        response_post_user_json = requests.post(self.domain + enter_point, data=payload, headers=headers).json()
        print(response_post_user_json)
        self.assertEqual(response_post_user_json['data'], 'strange=boom')

if __name__ == '__main__':
    unittest.main()
