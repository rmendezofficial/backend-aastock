from fastapi import FastAPI
from database import engine,SessionLocal,Base
from fastapi.middleware.cors import CORSMiddleware
from routers import users,companies

origins = [
    "https://stock.rcmendez.com",
    "http://localhost:3000", 
]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(users.router)
app.include_router(companies.router)

Base.metadata.create_all(bind=engine)
