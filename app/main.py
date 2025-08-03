from fastapi import FastAPI
from datetime import datetime
from models import Customer, Transaction, Invoice, Plan
from db import SessionDep, create_tables
from .routers import customers, transactions, plans


app = FastAPI(lifespan=create_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(plans.router)


@app.get("/")
async def root():
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

