import pandas as pd
import ta

def generate_signals(df):
    df = df.copy()
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()
    df['Buy'] = (df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])
    return df
