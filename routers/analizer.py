
import math


class Analizer():#analizar la data y retornar un nuevo json con la data y los analisis, llamarlo en la vista del backend y listo, enviar al front
    def __init__(self,company):
        self.company=company
        self.results=[]
    #qtotalrevenue=qincome.loc['Total Revenue']#.iloc[0]#el .iloc es para buscar un valor en particular
    #qgrossprofit=qincome.loc['Gross Profit']
    #totalrevenue=income.loc['Total Revenue']
    #grossprofit=income.loc['Gross Profit']
    #qtotalassets=qbalance.loc['Total Assets']
    #qtotalliabilities=qbalance.loc['Total Liabilities Net Minority Interest']
    #totalassets=balance.loc['Total Assets']
    #totalliabilities=balance.loc['Total Liabilities Net Minority Interest']
    #dividendyield=ticker.info.get('dividendYield')
    #qearningestimate=qearnings
    #stock=historical.iloc[-1]
    #eps = ticker.info.get('trailingEps') 
    #ps = ticker.info.get('priceToSalesTrailing12Months')
    #ordinary_shares = ticker.info.get('sharesOutstanding')
    
    def cleanData(self,name):
        q_total_revenue=self.company[f'{name}']
        results=[]
        counter=0
        for i in q_total_revenue:
            r=q_total_revenue.iloc[counter]
            counter+=1
            if not math.isnan(r):
                results.append(float(r))
        self.company[f'{name}']=results
    
    def cleanDataEstimate(self,name):
        q_total_revenue=self.company[f'{name}']['avg']
        results=[]
        counter=0
        for i in q_total_revenue:
            r=q_total_revenue.iloc[counter]
            counter+=1
            if not math.isnan(r):
                results.append(float(r))
        self.company[f'{name}']=results   
    
    def cleanStock(self,name):
        q_total_revenue=self.company[f'{name}']
        results=[]
        counter=0
        for i in q_total_revenue:
            r=q_total_revenue.iloc[counter]
            counter+=1
            if not math.isnan(r):
                results.append(float(r/100))                
        self.company[f'{name}']=results
        
    def evaluate_params(self):
        self.cleanData('qtotalrevenue')
        self.cleanData('qgrossprofit')
        self.cleanData('totalrevenue')     
        self.cleanData('grossprofit')
        self.cleanData('qtotalassets')
        self.cleanData('qtotalliabilities')
        self.cleanData('totalassets')
        self.cleanData('totalliabilities')
        self.cleanDataEstimate('qearningestimate')
        self.cleanStock('stock')
        


