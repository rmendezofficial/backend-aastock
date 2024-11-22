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
        bot.evaluate_params()
        db_company=Companies(
        user_id=user_id,
        name=bot.company['name'],
        qtotalrevenue=bot.company['qtotalrevenue'][0],
        qtotalrevenue1=bot.company['qtotalrevenue'][1],
        qtotalrevenue2=bot.company['qtotalrevenue'][2],
        qtotalrevenue3=bot.company['qtotalrevenue'][3],
        qgrossprofit=bot.company['qgrossprofit'][0],
        qgrossprofit1=bot.company['qgrossprofit'][1],
        qgrossprofit2=bot.company['qgrossprofit'][2],
        qgrossprofit3=bot.company['qgrossprofit'][3],
        totalrevenue=bot.company['totalrevenue'][0],
        totalrevenue1=bot.company['totalrevenue'][1],
        totalrevenue2=bot.company['totalrevenue'][2],
        totalrevenue3=bot.company['totalrevenue'][3],
        grossprofit=bot.company['grossprofit'][0],
        grossprofit1=bot.company['grossprofit'][1],
        grossprofit2=bot.company['grossprofit'][2],
        grossprofit3=bot.company['grossprofit'][3],
        qtotalassets=bot.company['qtotalassets'][0],
        qtotalassets1=bot.company['qtotalassets'][1],
        qtotalassets2=bot.company['qtotalassets'][2],
        qtotalassets3=bot.company['qtotalassets'][3],
        qtotalliabilities=bot.company['qtotalliabilities'][0],
        qtotalliabilities1=bot.company['qtotalliabilities'][1],
        qtotalliabilities2=bot.company['qtotalliabilities'][2],
        qtotalliabilities3=bot.company['qtotalliabilities'][3],
        totalassets=bot.company['totalassets'][0],
        totalassets1=bot.company['totalassets'][1],
        totalassets2=bot.company['totalassets'][2],
        totalassets3=bot.company['totalassets'][3],
        totalliabilities=bot.company['totalliabilities'][0],
        totalliabilities1=bot.company['totalliabilities'][1],
        totalliabilities2=bot.company['totalliabilities'][2],
        totalliabilities3=bot.company['totalliabilities'][3],
        dividendyield=bot.company['dividendyield'],
        qearningestimate=bot.company['qearningestimate'][0],
        qearningestimate1=bot.company['qearningestimate'][1],
        qearningestimate2=bot.company['qearningestimate'][2],
        qearningestimate3=bot.company['qearningestimate'][3],
        stock=bot.company['stock'][0],
        stock1=bot.company['stock'][1],
        stock2=bot.company['stock'][2],
        stock3=bot.company['stock'][3],
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
    company_db=db.query(Companies).filter(Companies.id==company_id).first()
    data_company=getData(f'{company_db.name}')
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
        db_company.qtotalrevenue=bot.company['qtotalrevenue'][0],
        db_company.qtotalrevenue1=bot.company['qtotalrevenue'][1],
        db_company.qtotalrevenue2=bot.company['qtotalrevenue'][2],
        db_company.qtotalrevenue3=bot.company['qtotalrevenue'][3],
        db_company.qgrossprofit=bot.company['qgrossprofit'][0],
        db_company.qgrossprofit1=bot.company['qgrossprofit'][1],
        db_company.qgrossprofit2=bot.company['qgrossprofit'][2],
        db_company.qgrossprofit3=bot.company['qgrossprofit'][3],
        db_company.totalrevenue=bot.company['totalrevenue'][0],
        db_company.totalrevenue1=bot.company['totalrevenue'][1],
        db_company.totalrevenue2=bot.company['totalrevenue'][2],
        db_company.totalrevenue3=bot.company['totalrevenue'][3],
        db_company.grossprofit=bot.company['grossprofit'][0],
        db_company.grossprofit1=bot.company['grossprofit'][1],
        db_company.grossprofit2=bot.company['grossprofit'][2],
        db_company.grossprofit3=bot.company['grossprofit'][3],
        db_company.qtotalassets=bot.company['qtotalassets'][0],
        db_company.qtotalassets1=bot.company['qtotalassets'][1],
        db_company.qtotalassets2=bot.company['qtotalassets'][2],
        db_company.qtotalassets3=bot.company['qtotalassets'][3],
        db_company.qtotalliabilities=bot.company['qtotalliabilities'][0],
        db_company.qtotalliabilities1=bot.company['qtotalliabilities'][1],
        db_company.qtotalliabilities2=bot.company['qtotalliabilities'][2],
        db_company.qtotalliabilities3=bot.company['qtotalliabilities'][3],
        db_company.totalassets=bot.company['totalassets'][0],
        db_company.totalassets1=bot.company['totalassets'][1],
        db_company.totalassets2=bot.company['totalassets'][2],
        db_company.totalassets3=bot.company['totalassets'][3],
        db_company.totalliabilities=bot.company['totalliabilities'][0],
        db_company.totalliabilities1=bot.company['totalliabilities'][1],
        db_company.totalliabilities2=bot.company['totalliabilities'][2],
        db_company.totalliabilities3=bot.company['totalliabilities'][3],
        db_company.dividendyield=bot.company['dividendyield'],
        db_company.qearningestimate=bot.company['qearningestimate'][0],
        db_company.qearningestimate1=bot.company['qearningestimate'][1],
        db_company.qearningestimate2=bot.company['qearningestimate'][2],
        db_company.qearningestimate3=bot.company['qearningestimate'][3],
        db_company.stock=bot.company['stock'][0],
        db_company.stock1=bot.company['stock'][1],
        db_company.stock2=bot.company['stock'][2],
        db_company.stock3=bot.company['stock'][3],
        db_company.eps=bot.company['eps'],
        db_company.ps=bot.company['ps'],
        db_company.ordinary_shares=bot.company['ordinary_shares']
        db.commit()
        return {'message':'User succesfuly updated'}
    return {'message':'CSRF FAILED'}





