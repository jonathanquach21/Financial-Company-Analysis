import yfinance as yf
import pandas as pd

tickers = ["AAPL", "NVDA", "GOOGL", "AMZN"]
rows = []

for ticker in tickers:
    company = yf.Ticker(ticker)

    income = company.income_stmt
    balance = company.balance_sheet
    cashflow = company.cashflow

    latest_year = income.columns[0]
    
    revenue = income.loc["Total Revenue", latest_year]
    gp = income.loc["Gross Profit", latest_year]
    net_income = income.loc["Net Income", latest_year]


    current_assets = balance.loc["Current Assets", latest_year]
    current_liabilites = balance.loc["Current Liabilities", latest_year]
    total_debt = balance.loc["Total Debt", latest_year]
    equity = balance.loc["Stockholders Equity", latest_year]

    operating_cash_flow = cashflow.loc["Operating Cash Flow", latest_year]
    capex = cashflow.loc["Capital Expenditure", latest_year]

    current_ratio = current_assets / current_liabilites
    debt_equity = total_debt / equity
    gross_marign = gp / revenue
    net_margin = net_income / revenue


    rows.append({
        "Ticker": ticker,
        "Revenue": revenue,
        "Current Ratio": current_ratio,
        "Debt to Equity": debt_equity,
        "Gross Margin": gross_marign,
        "Net Margin": net_margin
    })

    df = pd.DataFrame(rows)
    
df["Profitability Rank"] = df["Net Margin"].rank(ascending=False)
df["Liquidity Rank"] = df["Current Ratio"].rank(ascending=False)
df["Debt Rank"] = df["Debt to Equity"].rank(ascending=True)    
print(df)



