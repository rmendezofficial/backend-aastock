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
    name=Column(String(50),unique=True)
    qtotalrevenue=Column(Float,default=None)
    qgrossprofit=Column(Float,default=None)
    totalrevenue=Column(Float,default=None)
    grossprofit=Column(Float,default=None)
    qtotalassets=Column(Float,default=None)
    qtotalliabilities=Column(Float,default=None)
    totalassets=Column(Float,default=None)
    totalliabilities=Column(Float,default=None)
    dividendyield=Column(Float,default=None)
    qearningestimate=Column(Float,default=None)    
    stock=Column(Float,default=None)
    eps=Column(Float,default=None)
    ps=Column(Float,default=None)
    ordinary_shares=Column(Float,default=None)
