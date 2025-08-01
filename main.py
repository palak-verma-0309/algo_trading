from data_fetcher import fetch_data
from strategy import generate_signals, backtest_strategy
from ml_model import train_model
from sheet_logger import authorize_sheets, log_to_sheet
from telegram_alert import send_telegram_message

import pandas as pd
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
json_keyfile = "credentials.json"
sheet_name = "Algo_trade"
client = authorize_sheets(json_keyfile)

for stock in stocks:
    try:
        print(f"\nProcessing {stock}...")
        df = fetch_data(stock)
        signals_df = generate_signals(df)
        bt_df = backtest_strategy(df)
        model, accuracy = train_model(signals_df)

        trade_log = signals_df.tail(10)[['Close', 'RSI', '20DMA', '50DMA', 'Buy']]
        log_to_sheet(client, sheet_name, f"{stock}_Trade Log", trade_log)

        win_ratio = trade_log['Buy'].sum() / len(trade_log)
        pnl_summary = pd.DataFrame({
            'Model Accuracy': [accuracy],
            'Win Ratio': [win_ratio]
        })
        log_to_sheet(client, sheet_name, f"{stock}_P&L Summary", pnl_summary)

        send_telegram_message(f"{stock}: Processed successfully. Accuracy: {accuracy:.2f}, Win Ratio: {win_ratio:.2f}")
    
    except Exception as e:
        error_msg = f"Error processing {stock}: {str(e)}"
        print(error_msg)
        send_telegram_message(error_msg)
