## Section 3

- `14_ib_basic_app.py`: Wrappers and establish connection
- `15_ib_contract_intro.py`: Get stock info (contract) and print contract details
- `16_ib_contract_asynch.py`: Quit the program automatically with daemon thread for `app.run()` after the main program finishes running. (Solution for persistent connection problem)
  - **Note:** this program is not quitting properly the app.run() method blocks the thread where it was executed, so if you want to disconnect from the app, you have to run it from different thread. Issue fixed in `17_ib_contract_asynch_event.py`
- `17_ib_contract_asynch_event.py`: Use `Event` to resolved the persistent connection problem. Original code does not work for the same reason in `16_ib_contract_asynch.py`. Fixed with the source below
  - [Issue Source](https://www.udemy.com/course/algorithmic-trading-using-interactive-brokers-python-api/learn/lecture/22211930#questions/12709998)
