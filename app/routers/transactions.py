from fastapi.params import Query
from models import Customer, Transaction, TransactionCreate
from db import SessionDep
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select


router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_transation(
    transaction_data: TransactionCreate,
    session: SessionDep
):
    transaction_data_dict = transaction_data.model_dump()
    customer = session.get(Customer, transaction_data_dict.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer doesn't exist"
        )

    transaction_db = Transaction.model_validate(transaction_data_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)

    return transaction_db


@router.get("/")
async def get_transactions(
    session: SessionDep,
    skip: int = Query(0, description="Number of transactions to skip"),
    limit: int = Query(10, description="Maximum number of transactions to return")
):
    query = select(Transaction).offset(skip).limit(limit)
    transactions = session.exec(query).all()
    return transactions
