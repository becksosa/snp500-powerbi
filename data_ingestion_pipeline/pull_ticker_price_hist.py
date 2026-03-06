import yfinance as yf


def pull_ticker_price_hist(ticker: str) -> list[dict]:
    stock = yf.Ticker(ticker)
    hist = stock.history(start="2020-01-01", end="2025-12-31")

    if hist.empty:
        raise ValueError(f"No data returned for {ticker}")

    hist = hist.reset_index()

    records = []
    for _, row in hist.iterrows():
        records.append({
            "ticker":    ticker,
            "date":      row["Date"].date(),
            "open":      round(float(row["Open"]), 4),
            "high":      round(float(row["High"]), 4),
            "low":       round(float(row["Low"]), 4),
            "close":     round(float(row["Close"]), 4),
            "volume":    int(row["Volume"]),
            "dividends": round(float(row["Dividends"]), 6),
        })
    return records
