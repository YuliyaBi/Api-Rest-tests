#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):
        print 'get_in_test started'
        request = requests.get('http://services.groupkt.com/country/get/iso2code/IN')
        print 'Assert status code: 200 OK'

        #print request.json['RestResponse']['result']
        data = request.json()

        self.assertEqual(data['RestResponse']['result']['name'], 'India')
        self.assertEqual(data['RestResponse']['result']['alpha2_code'], 'IN')
        self.assertEqual(data['RestResponse']['result']['alpha3_code'], 'IND')

        print 'response json looks good OK'


        self.assertEqual(200, request.status_code)
        print 'get_in_test passed'

if __name__ == '__main__':
    unittest.main()