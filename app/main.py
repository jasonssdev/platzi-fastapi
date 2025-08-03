from typing import Annotated
from fastapi import FastAPI, Request
from datetime import datetime

from fastapi.params import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import Customer, Transaction, Invoice, Plan
from db import SessionDep, create_tables
from .routers import customers, transactions, plans
import time


app = FastAPI(lifespan=create_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(plans.router)


@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.method} {request.url} - Processed in {process_time:.4f} seconds")
    return response


security = HTTPBasic()

@app.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print(credentials)
    return {"message": "Hello World"}


@app.get("/time")
async def get_time():
    time_now = datetime.now()
    return {
        "current_time": time_now.strftime("%Y-%m-%d %H:%M:%S"),
    }


@app.post("/invoices/")
async def create_invoice(invoice_data: Invoice, session: SessionDep):
    invoice = Invoice.model_validate(invoice_data.model_dump())
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice

