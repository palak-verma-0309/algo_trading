from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def train_model(df):
    df = df.dropna()
    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)
    X = df[['RSI', '20DMA', '50DMA']]
    y = df['Target']
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    preds = clf.predict(X)
    acc = accuracy_score(y, preds)
    return clf, acc
