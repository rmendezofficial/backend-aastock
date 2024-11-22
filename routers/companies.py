from fastapi import FastAPI,HTTPException,Depends,status, APIRouter,Request
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine,SessionLocal,Base
from sqlalchemy.orm import Session
import os
from database import database_db
from models import Users,Companies
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
import secrets
from fastapi.responses import JSONResponse
#from .analizer import Analizer
#from .getdata import getData
#from getdata import getData
import math
import yfinance as yf
from .users import current_user
from .getdata import getData
from .analizer import Analizer
 
router=APIRouter(prefix='/companies',responses={404:{'message':'No encontrado'}})

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

    
    
    
        
@router.get('/',status_code=status.HTTP_200_OK)
def get_companies(db:Session=Depends(get_db)):
    data_company=list(db.query(Companies))    
    data={'data':data_company}
    return data

@router.get('/search',status_code=status.HTTP_200_OK)
async def search_company(query:str,db:Session=Depends(get_db)):
    data=getData(f'{query}')
    bot=Analizer(data)
    bot.evaluate_params()
    final_data={'data':bot.company}
    return final_data
    
@router.post('/add_company',status_code=status.HTTP_201_CREATED)
def add_company(request:Request,user_id:int,company:str,db:Session=Depends(get_db),user_auth:Users=Depends(current_user)):
    
    user=db.query(Users).filter(Users.id==user_id).first()
    csrf_token_db=user.token
    csrf_token_req=request.cookies.get('csrf_token')
    if csrf_token_db==csrf_token_req:
        data_company=getData(company)
        bot=Analizer(data_company)
        db_company=Companies(
        user_id=user_id,
        name=bot.company['name'],
        qtotalrevenue=bot.company['qtotalrevenue'],
        qgrossprofit=bot.company['qgrossprofit'],
        totalrevenue=bot.company['totalrevenue'],
        grossprofit=bot.company['grossprofit'],
        qtotalassets=bot.company['qtotalassets'],
        qtotalliabilities=bot.company['qtotalliabilities'],
        totalassets=bot.company['totalassets'],
        totalliabilities=bot.company['totalliabilities'],
        dividendyield=bot.company['dividendyield'],
        qearningestimate=bot.company['qearningestimate'],    
        stock=bot.company['stock'],
        eps=bot.company['eps'],
        ps=bot.company['ps'],
        ordinary_shares=bot.company['ordinary_shares']
            )
        db.add(db_company)
        db.commit()
        return{'message':'Post successfuly created'}
    return {'message':'CSRF FAILED'}
    
@router.delete('/delete_company',status_code=status.HTTP_200_OK)
async def delete_company(request:Request,company_id:int,db:Session=Depends(get_db),user_auth:Users=Depends(current_user)):
    company_db=db.query(Companies).filter(Companies.id==company_id).first()
    user=db.query(Users).filter(Users.id==company_db.user_id).first()
    csrf_token_db=user.token
    csrf_token_req=request.cookies.get('csrf_token')
    if csrf_token_db==csrf_token_req:
        db.delete(company_db)
        db.commit()
        return {'message':'Post succesfuly deleted'}
    return {'message':'CSRF FAILED'}
    
@router.get('/get_company/{company_id}',status_code=status.HTTP_200_OK)
async def get_company(company_id:int,db:Session=Depends(get_db)):
    data_company=getData('AMZN')
    bot=Analizer(data_company)
    bot.evaluate_params()
    data={'data':bot.company}
    return data


@router.put('/update_company')
async def update_company(request:Request,user_id:int,company_id:int,db:Session=Depends(get_db),user_auth:Users=Depends(current_user)):
    user_db=db.query(Users).filter(Users.id==user_id).first()
    csrf_token_db=user_db.token
    csrf_token_req=request.cookies.get('csrf_token')
    if csrf_token_db==csrf_token_req:
        db_company=db.query(Companies).filter(Companies.id==company_id).first()
        company_data_new=getData(db_company.name)
        bot=Analizer(company_data_new)
        bot.evaluate_params()
        db_company.qtotalrevenue=bot.company['qtotalrevenue'],
        db_company.qgrossprofit=bot.company['qgrossprofit'],
        db_company.totalrevenue=bot.company['totalrevenue'],
        db_company.grossprofit=bot.company['grossprofit'],
        db_company.qtotalassets=bot.company['qtotalassets'],
        db_company.qtotalliabilities=bot.company['qtotalliabilities'],
        db_company.totalassets=bot.company['totalassets'],
        db_company.totalliabilities=bot.company['totalliabilities'],
        db_company.dividendyield=bot.company['dividendyield'],
        db_company.qearningestimate=bot.company['qearningestimate'],    
        db_company.stock=bot.company['stock'],
        db_company.eps=bot.company['eps'],
        db_company.ps=bot.company['ps'],
        db_company.ordinary_shares=bot.company['ordinary_shares']
        db.commit()
        return {'message':'User succesfuly updated'}
    return {'message':'CSRF FAILED'}





