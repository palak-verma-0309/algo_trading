from data_fetcher import fetch_data
from strategy import generate_signals, backtest_strategy
from ml_model import train_model
from sheet_logger import authorize_sheets, log_to_sheet
from telegram_alert import send_telegram_message
import pandas as pd
try:
    df = fetch_data("RELIANCE.NS")
    signals_df = generate_signals(df)
    bt_df = backtest_strategy(df)
    model, accuracy = train_model(signals_df)
    last_signal = signals_df.iloc[-1]
    if last_signal['Buy']:
        send_telegram_message(f"BUY Signal Triggered for RELIANCE.NS at ₹{last_signal['Close']:.2f}")
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

except Exception as e:
    send_telegram_message(f"Error occurred: {str(e)}")
    raise
