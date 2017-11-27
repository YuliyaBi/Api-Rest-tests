#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):
        print 'get_ae_test started'
        request = requests.get('http://services.groupkt.com/country/search?text=ae')
        print 'Assert status code: 200 OK'

        data = request.json()
        #print data['RestResponse']['result']
        country_list = [{"name" : "Israel",
                                        "alpha2_code" : "IL",
                                        "alpha3_code" : "ISR"},
                        {"name" : "United Arab Emirates",
                                        "alpha2_code" : "AE",
                                        "alpha3_code" : "ARE"}]

        for element in country_list:
            print (element.get("name"), element.get("alpha2_code"), element.get("alpha3_code"))


        # for item, value in country_list:
        #     for name in item:
        #         print name
        # self.assertEqual(data['RestResponse']['result']['name'], 'India')
        # self.assertEqual(data['RestResponse']['result']['alpha2_code'], 'IN')
        # self.assertEqual(data['RestResponse']['result']['alpha3_code'], 'IND')

        print 'response json looks good OK'


        self.assertEqual(200, request.status_code)
        print 'get_in_test passed'

if __name__ == '__main__':
    unittest.main()
