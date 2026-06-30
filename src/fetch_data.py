import yfinance as yf
import pandas as pd

def fetch_yfinance(tickers: str = "SPY",
                   period: str = "5d",
                   interval: str = "5m",
                   auto_adjust: bool = True
                   ) -> pd.DataFrame:
    
    """
    Input interested market or equities, time horizon and frequency of measurement.
    Pull the corresponding dataframe from yfinance and output a dataframe.
    User can choose to use adjusted price or not by adjusting the auto_adjust variable.
    """

    data = yf.download(tickers=tickers,
                       period=period,
                       interval=interval,
                       auto_adjust=auto_adjust)

    return data

if __name__ == "__main__":
    print("Testing: fetch_data.py")
    df = fetch_yfinance()
    print(df.head())
