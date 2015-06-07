'''
Created on 2015

@author: aadebuger
'''
import unittest
import logging

from zpay import Entity
from pingpp import error, http_client, version, util, certificate_blacklist
class Test(unittest.TestCase):


    def testName(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
#        util.logger =logger
        util.logger.setLevel(logging.DEBUG)
#        Entity.getEvent()
    def testCharge(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
#        util.logger =logger
        util.logger.setLevel(logging.DEBUG)
        Entity.charge()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()