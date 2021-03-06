# -*- coding: utf-8 -*-
"""
IBAPI - Getting Contract info

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId,errorCode,errorString))

    def contractDetails(self, reqId, contractDetails):
        print("redID: {}, contract:{}".format(reqId,contractDetails))


def websocket_con():
    app.run()


def stop_app():
    print('Waiting for close event')
    close_event.wait() # (optional) indicates waiting for the event to happen
    if close_event.is_set(): # will get triggered after close_event.set()
        app.disconnect()
        print('Client is disconnecting')


close_event = threading.Event()
app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)

# starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established

# add a close even thread since the app.run() method blocks the thread where
# it was executed, so if you want to disconnect from the app, you have to run
# it from different thread
stop_app_thread = threading.Thread(target=stop_app)
stop_app_thread.start();

#creating object of the Contract class - will be used as a parameter for other function calls
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract) # EClient function to request contract details
time.sleep(5) # some latency added to ensure that the contract details request has been processed
close_event.set()
