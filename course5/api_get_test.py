import unittest

import requests


class TestStringMethods(unittest.TestCase):
    domain = 'https://postman-echo.com'

    def test_get_user(self):
        enter_point = '/get'

        payload = {'user': 'jim'}
        response_get_user_json = requests.get(self.domain + enter_point, params=payload).json()
        print(response_get_user_json)
        self.assertEqual(response_get_user_json['args']['user'], 'jim')

    def test_post_stange(self):
        enter_point="post"
        payload = {'strange': 'boom'}
        response_get_user_json = requests.post(self.domain + enter_point, params=payload).json()
        self.assertEqual(response_get_user_json['form']['strange'], 'boom')


if __name__ == '__main__':
    unittest.main()
