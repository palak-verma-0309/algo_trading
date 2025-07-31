import pandas as pd
import ta

def generate_signals(df):
    df = df.copy()
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()
    df['Buy'] = (df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])
    return df

def backtest_strategy(df, initial_capital=100000):
    df = generate_signals(df)
    df['Position'] = df['Buy'].shift(1)
    df['Returns'] = df['Close'].pct_change()
    df['Strategy'] = df['Returns'] * df['Position'].fillna(0)
    df['Equity'] = (1 + df['Strategy']).cumprod() * initial_capital
    return df
