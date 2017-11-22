#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):
        print 'get_usa_test started'
        request = requests.get('http://services.groupkt.com/country/get/iso3code/USA')
        print 'Assert status code: 200 OK'

        data = request.json()

        self.assertEqual(data['RestResponse']['result']['name'], 'United States of America')
        self.assertEqual(data['RestResponse']['result']['alpha2_code'], 'US')
        self.assertEqual(data['RestResponse']['result']['alpha3_code'], 'USA')

        print 'response json looks good OK'


        self.assertEqual(200, request.status_code)
        print 'get_usa_test passed'

if __name__ == '__main__':
    unittest.main()