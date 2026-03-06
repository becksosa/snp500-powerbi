import time
import pandas as pd
import psycopg2
from pull_ticker_data import pull_ticker_data
from run_query import run_query
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

# get all tickers
snp = run_query(
    """select ticker from sp500
  order by ticker asc;""")


all_data = []

# pull data for each ticker
for t in snp:
    ticker = t[0]
    try:
        data = pull_ticker_data(ticker)
        all_data.append(data)
        print(f"pulled data for {ticker}")
    except Exception as e:
        print(f"ts faled for {ticker}: {e}")
    time.sleep(0.3)

# make it a df
df = pd.DataFrame(all_data)

# create connection to postgres
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('POSTGRES_DB')}"
)

# put data into SQL
df.to_sql("ticker_data", engine, if_exists="append", index=False)
