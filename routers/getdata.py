import yfinance as yf

def getData(company):
    ticker=yf.Ticker(f'{company}')
    qfinancials=ticker.quarterly_financials
    qbalance=ticker.quarterly_balancesheet
    qincome=ticker.quarterly_incomestmt
    qhistorical=ticker.history(period='max')
    qearnings=ticker.earnings_estimate
    
    financials=ticker.financials
    balance=ticker.balancesheet
    income=ticker.incomestmt
    historical=ticker.history(period='max')
    dividends=ticker.dividends
    
    
    qtotalrevenue=qincome.loc['Total Revenue']#.iloc[0]#el .iloc es para buscar un valor en particular
    qgrossprofit=qincome.loc['Gross Profit']
    totalrevenue=income.loc['Total Revenue']
    grossprofit=income.loc['Gross Profit']
    qtotalassets=qbalance.loc['Total Assets']
    qtotalliabilities=qbalance.loc['Total Liabilities Net Minority Interest']
    totalassets=balance.loc['Total Assets']
    totalliabilities=balance.loc['Total Liabilities Net Minority Interest']
    dividendyield=ticker.info.get('dividendYield')
    qearningestimate=qearnings
    stock=historical.iloc[-1]
    eps = ticker.info.get('trailingEps') 
    ps = ticker.info.get('priceToSalesTrailing12Months')
    ordinary_shares = ticker.info.get('sharesOutstanding')
    
    data={
        'name':f'{company}',
        'qtotalrevenue':qtotalrevenue,'qgrossprofit':qgrossprofit,
        'totalrevenue':totalrevenue,'grossprofit':grossprofit,
        'qtotalassets':qtotalassets,'qtotalliabilities':qtotalliabilities,
        'totalassets':totalassets,'totalliabilities':totalliabilities,
        'dividendyield':dividendyield,
        'qearningestimate':qearningestimate,
        'stock':stock,
        'eps':eps,
        'ps':ps,
        'ordinary_shares':ordinary_shares
        }
    return data
  
    
