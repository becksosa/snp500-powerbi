import yfinance as yf


def pull_ticker_data(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info

# pull a bunch of general info
    general = {
        # Identification
        "symbol":                  info.get("symbol"),
        "company_name":            info.get("longName"),
        "sector":                  info.get("sector"),
        "industry":                info.get("industry"),
        "market_cap":              info.get("marketCap"),

        # Valuation
        "pe_trailing":             info.get("trailingPE"),
        "pe_forward":              info.get("forwardPE"),
        "price_to_sales":          info.get("priceToSalesTrailing12Months"),
        "price_to_book":           info.get("priceToBook"),
        "ev_to_ebitda":            info.get("enterpriseToEbitda"),
        "peg_ratio":               info.get("pegRatio"),

        # Profitability
        "profit_margin":           info.get("profitMargins"),
        "operating_margin":        info.get("operatingMargins"),
        "roe":                     info.get("returnOnEquity"),
        "roa":                     info.get("returnOnAssets"),

        # Financial Health
        "debt_to_equity":          info.get("debtToEquity"),
        "current_ratio":           info.get("currentRatio"),
        "free_cash_flow":          info.get("freeCashflow"),
        "cash":                    info.get("totalCash"),

        # Dividends
        "dividend_yield":          info.get("dividendYield"),
        "payout_ratio":            info.get("payoutRatio"),
        "five_yr_avg_dividend":    info.get("fiveYearAvgDividendYield"),

        # Analyst Sentiment
        "analyst_recommendation":  info.get("recommendationKey"),
        "num_analyst_opinions":    info.get("numberOfAnalystOpinions"),
        "target_price":            info.get("targetMeanPrice"),
        "beta":                    info.get("beta"),
    }

# pull recent earnings
    earnings = ticker.earnings_history
    if earnings is not None and not earnings.empty:
        latest = earnings.iloc[-1]
        general["eps_actual"] = latest.get("epsActual")
        general["eps_estimate"] = latest.get("epsEstimate")
        general["eps_surprise_pct"] = latest.get("surprisePercent")
        general["earnings_date"] = latest.name  # date is the index

# pull recent revenue and calculate QoQ growth
    financials = ticker.quarterly_financials
    if financials is not None and not financials.empty and "Total Revenue" in financials.index:
        revenue = financials.loc["Total Revenue"]
        general["revenue_recent"] = revenue.iloc[0]
        general["revenue_prior"] = revenue.iloc[1]
        general["revenue_qoq_growth"] = round(
            (revenue.iloc[0] - revenue.iloc[1]) / revenue.iloc[1] * 100, 2
        )

    return general


# test
# data = pull_ticker_data("AAPL")

# for k, v in data.items():
#     print(f"{k:30s} {v}")
