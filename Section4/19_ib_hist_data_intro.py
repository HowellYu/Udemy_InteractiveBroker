# -*- coding: utf-8 -*-
"""
IBAPI - Getting historical data intro

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

    def historicalData(self, reqId, bar):
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)


def websocket_con():
    app.run()

app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)

# starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established

#creating object of the Contract class - will be used as a parameter for other function calls
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "ISLAND" # change to ISLAND

app.reqHistoricalData(reqId=1,
                      contract=contract,
                      endDateTime='', # present
                      durationStr='3 M', # S(econd) D W M Y
                      barSizeSetting='5 mins', # check doc here http://interactivebrokers.github.io/tws-api/historical_bars.html
                      whatToShow='MIDPOINT', # MIDPOINT takes midpoint for bid/ask, there is no volume for bid/ask. Volume only make sense for executed order 
                      useRTH=1,
                      formatDate=1,
                      keepUpToDate=0,
                      chartOptions=[])	 # EClient function to request contract details
time.sleep(5) # some latency added to ensure that the contract details request has been processed
