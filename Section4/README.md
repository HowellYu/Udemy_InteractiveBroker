### Section 4: Historical Data

> We are going to work the most with History Bar Data

- `19_ib_hist_data_intro.py`: obtain historical data
  - Bar data includes:
    - high
    - low
    - open
    - close
    - volume
    - count
    - wap
  - [Doc here](http://interactivebrokers.github.io/tws-api/historical_data.html)
  - There will be no "volume" for "midpoint" option while retrieving historical data.
  - "volume" has unit in 1k
- `20_ib_hist_multi_ticker.py` & `20_ib_hist_multi_fx_pairs.py`: `19` + for loop
- `21_ib_hist_dataframe.py`
- `22_ib_hist_dataframe_event.py`
- `23_ib_hist_iterative.py`: Introduced an iterative way of ingesting data after a period of time
- `24_ib_hist_general_stk.py`: Storing historical data of stocks from different exchanges
