from data_fetcher import fetch_data
from strategy import generate_signals

df = fetch_data("RELIANCE.NS")
print(df.tail())
signals_df = generate_signals(df)
print(signals_df[['Close', 'RSI', '20DMA', '50DMA', 'Buy']].tail())
