import yfinance as yf
import pandas as pd

def fetch_data(symbol, period="6mo", interval="1d"):
    data = yf.download(symbol, period=period, interval=interval)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]
    print(f"Fetched {len(data)} rows for {symbol}")
    return data