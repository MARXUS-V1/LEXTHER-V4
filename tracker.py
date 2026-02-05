import yfinance as yf
from datetime import datetime

#List of stocks to track
tickers = ["AAPL", "TSLA", "BTC-USD"]

print(f"market update:")
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                         
print("-"*30)

for ticker in tickers:
  data=yf.Ticker(ticker)
  price=data.history(periods=1d")
  ['Close'].iloc[-1]
  print(f"{ticker}:${price:.2f}")
