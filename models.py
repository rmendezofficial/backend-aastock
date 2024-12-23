from sqlalchemy import Boolean,Column,Integer,String,DateTime,Text,Float
from database import Base
from sqlalchemy.sql import func

class Users(Base):
    __tablename__='users'
    
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True)
    password=Column(String(200))
    email=Column(String(100))
    disabled=Column(Boolean,default=False)
    token=Column(String(200),default=None)

class Companies(Base):
    __tablename__='companies'
    
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer)
    name=Column(String(50))
    qtotalrevenue=Column(Float,default=None)
    qtotalrevenue1=Column(Float,default=None)
    qtotalrevenue2=Column(Float,default=None)
    qtotalrevenue3=Column(Float,default=None)
    qgrossprofit=Column(Float,default=None)
    qgrossprofit1=Column(Float,default=None)
    qgrossprofit2=Column(Float,default=None)    
    qgrossprofit3=Column(Float,default=None)
    totalrevenue=Column(Float,default=None)
    totalrevenue1=Column(Float,default=None)
    totalrevenue2=Column(Float,default=None)
    totalrevenue3=Column(Float,default=None)
    grossprofit=Column(Float,default=None)
    grossprofit1=Column(Float,default=None)
    grossprofit2=Column(Float,default=None)
    grossprofit3=Column(Float,default=None)
    qtotalassets=Column(Float,default=None)
    qtotalassets1=Column(Float,default=None)
    qtotalassets2=Column(Float,default=None)
    qtotalassets3=Column(Float,default=None)
    qtotalliabilities=Column(Float,default=None)
    qtotalliabilities1=Column(Float,default=None)
    qtotalliabilities2=Column(Float,default=None)
    qtotalliabilities3=Column(Float,default=None)
    totalassets=Column(Float,default=None)
    totalassets1=Column(Float,default=None)
    totalassets2=Column(Float,default=None)
    totalassets3=Column(Float,default=None)
    totalliabilities=Column(Float,default=None)
    totalliabilities1=Column(Float,default=None)
    totalliabilities2=Column(Float,default=None)
    totalliabilities3=Column(Float,default=None)
    dividendyield=Column(Float,default=None)
    qearningestimate=Column(Float,default=None)  
    qearningestimate1=Column(Float,default=None)  
    qearningestimate2=Column(Float,default=None)  
    qearningestimate3=Column(Float,default=None)    
    stock=Column(Float,default=None)
    stock1=Column(Float,default=None)
    stock2=Column(Float,default=None)
    stock3=Column(Float,default=None)
    eps=Column(Float,default=None)
    ps=Column(Float,default=None)
    ordinary_shares=Column(Float,default=None)

