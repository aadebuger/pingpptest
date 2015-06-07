'''
Created on 2015

@author: aadebuger
'''

import pingpp
import json
import random
import string
import os
import logging
from pingpp import error, http_client, version, util, certificate_blacklist
pingpp.api_key = 'sk_test_eTebX11mv5iDPWDujP100C88'

#pingpp.api_key = 'sk_test_eTebX11mv5iDPWDujP100C88'

pingpp.api_base="http://localhost:5000"

def getEvent():
    pingpp.verify_ssl_certs=False
    eve = pingpp.Event.all()
    print eve
def charge():
    util.logger.setLevel(logging.INFO)
            
    pingpp.verify_ssl_certs=False
    
    orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    form={}
    if isinstance(form, dict):
        form['order_no'] = orderno
        form['app'] = dict(id=os.environ.get('PINGPP_APP_ID',"app_u1KGKKW1OeX58CCu"))
        form['currency'] = "cny"
        form['client_ip'] = "127.0.0.1"
        form['subject'] = "Your Subject"
        form['body'] = "Your Body"
        form['channel']="wx"
        form['amount']=888
    print form
    pingpp.api_key = os.environ.get('PINGPP_APP_KEY',"sk_test_eTebX11mv5iDPWDujP100C88")
    response_charge = pingpp.Charge.create(api_key=pingpp.api_key, **form)
    print "Response_Charge: " + str(response_charge)
     
    
if __name__ == '__main__':
    pass