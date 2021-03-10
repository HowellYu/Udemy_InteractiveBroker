# -*- coding: utf-8 -*-
"""
IBAPI - EClient and EWrapper classes intro

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

# use these 2 classes to establish connection
from ibapi.client import EClient # hook up our port with TWS, make a connection
from ibapi.wrapper import EWrapper # obtain data and convert to python readable format
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId,errorCode,errorString))

app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1) # since we can have multiple connection to TWS
app.run()

time.sleep(3)
app.disconnect() # since it's a socket conenction not a http, it doesn't stop automatically
