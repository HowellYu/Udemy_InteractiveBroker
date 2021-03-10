# -*- coding: utf-8 -*-
"""
IB API - Daemon Threads

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

import threading
import time

def NumGen():
    for a in range(30): # w/o daemon, will print 30 numbers
                        # w/ daemon, will print ~ 10 numbers since greetings stops at 10
        print(a)
        time.sleep(1)

# daemon programs get terminated as soon as the main program terminates
thr2 = threading.Thread(target=NumGen) #creating a separate thread to execute the NumGen function
thr2.daemon=True #defining a thread as daemon thread
# thr2 = threading.Thread(target=NumGen, daemon=True)
thr2.start() #start execution of NumGen function on the parallel thread

def greeting():
    for i in range(10):
        print("Hello")
        time.sleep(1)
greeting()
