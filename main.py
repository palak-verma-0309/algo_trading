from data_fetcher import fetch_data
from strategy import generate_signals,backtest_strategy
from ml_model import train_model
df = fetch_data("RELIANCE.NS")
print(df.tail())
signals_df = generate_signals(df)
print(signals_df[['Close', 'RSI', '20DMA', '50DMA', 'Buy']].tail())
bt_df = backtest_strategy(df)
print(bt_df[['Equity']].tail())
model, accuracy = train_model(signals_df)
print("Model Accuracy:", accuracy)