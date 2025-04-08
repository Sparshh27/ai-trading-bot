import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict_price(ticker_symbol):
    data = yf.download(ticker_symbol, period="1y", interval="1d")
    data = data.reset_index()

    data['Days'] = np.arange(len(data)).reshape(-1, 1)
    prices = data['Close'].values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(data[['Days']], prices)

    next_day = np.array([[len(data)]])
    prediction = model.predict(next_day)

    return round(float(prediction[0][0]), 2)
