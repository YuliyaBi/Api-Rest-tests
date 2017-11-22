#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):
        print 'get_ui_test started'
        request = requests.get('http://services.groupkt.com/country/get/iso3code/UI')
        print 'Assert status code: 200 OK'

        data = request.json()

        self.assertEqual(data['RestResponse']['messages'], ['No matching country found for requested code [UI].'])

        print 'response json looks good OK'


        self.assertEqual(200, request.status_code)
        print 'get_ui_test passed'

if __name__ == '__main__':
    unittest.main()