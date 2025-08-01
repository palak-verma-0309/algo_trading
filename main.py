from data_fetcher import fetch_data
from strategy import generate_signals,backtest_strategy
from ml_model import train_model
from sheet_logger import authorize_sheets, log_to_sheet
import pandas as pd

df = fetch_data("RELIANCE.NS")
signals_df = generate_signals(df)
bt_df = backtest_strategy(df)
model, accuracy = train_model(signals_df)

json_keyfile = "credentials.json"
sheet_name = "Algo_trade"

client = authorize_sheets(json_keyfile)

trade_log = signals_df.tail(10)[['Close', 'RSI', '20DMA', '50DMA', 'Buy']]
log_to_sheet(client, sheet_name, "Trade Log", trade_log)

win_ratio = trade_log['Buy'].sum() / len(trade_log)
pnl_summary = pd.DataFrame({
    'Model Accuracy': [accuracy],
    'Win Ratio': [win_ratio]
})
log_to_sheet(client, sheet_name, "P&L Summary", pnl_summary)