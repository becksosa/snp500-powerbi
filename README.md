# S&P 500 Report - Power BI
In this project I create an interactive report with visualizations and KPIs from the 2025 Q4 earnings report of all stocks included in the S&P500 using python for data ingestion, SQL for storage/querying of relational databases, and Power BI for data visualization.

To get the data I created a simple data ingestion pipleine with python which is included in the repo [here](/data_ingestion_pipeline/). I won't go into too much detail on how I acquired the data because the main focus of this project is the Power BI report.

I include photos of the Power BI dashboards in the description of the project below, however the PBIX file is also included in the repo if you would prefer it to be interactive. See [here](/Q4_Earnings.pbix).

### Data Ingestion Pipeline
Libraries: yfinance pandas, sqlalchemy, and psycopg2
 - Step one: I downloaded a CSV containing the current tickers in the S&P500 from [here](https://stockanalysis.com/list/sp-500-stocks/) and inserted it into my PostgreSQL database
 - Step two: created a python script which pulled a large variety of data about each ticker, using psycopg2 to talk to my SQL database, and yfinance to pull the data from the Yahoo Finance unofficial API
 - Step three: insert the data pulled back into my SQL database using sqlalchemy

# The Power BI Report
## S&P500 Treemap
The first and simplest page of the report is a treemap which gives you an idea of the relative portion each sector/industry takes up in the S&P500 based off of market cap.

![treemap](/assets/treemap.png)

## Per Sector Dashboard
The second page of the report is a detailed dashboard which provides a number of insights about each sector present in the S&P500, utilizing a slicer to switch between them.
 - Biggest winners and losers of Q4 based in revenue growth/decline
 - Revenue growth for Q4 for the entire sector
 - Beta for the entire sector
 - A chart plotting forward PE vs revenue growth, with each point on the plot representing a different stock, sized relative to it's market cap
 - What % of the total S&P500 market cap the selected sector is
 - Insight into analyst sentiment showing how many stocks are ranked as strong buy, buy, and hold
 - A treemap that shows red for industries with negative Q4 revenue, and green for those with positive Q4 revenue

I've included photos of of dashboards for three sectors below:

![basic_mats](/assets/basic_mats.png)

![tech](/assets/tech.png)

![consumer_defensive](/assets/consumer_defensive.png)

## Per Ticker Dashboard
The final page of the report is a dashboard which allows the viewer to drill down and analyze one stock at a time, again using a slicer as a filter. It contains visualizations, key data points, and other information:
 - A visualization which plots stock price over time during Q4
 - Stock name, sector, industry, beta, and market cap
 - Anlalyst sentiment: strong buy, buy, or hold
 - Target price
 - A wide variety of other metrics viewable below the stock price chart

I've included photos of dashboards three for tickers below:

![amzn](/assets/amzn.png)

![aapl](/assets/aapl.png)

![bmy](/assets/bmy.png)
