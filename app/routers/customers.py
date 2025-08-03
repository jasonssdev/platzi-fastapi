from models import Customer, CustomerCreate, CustomerUpdate, CustomerPlan, Plan, StatusEnum
from db import SessionDep
from fastapi import APIRouter, HTTPException, status, Query
from sqlmodel import select


router = APIRouter(prefix="/customers", tags=["customers"])

db_customers: list[Customer] = []


@router.post("/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@router.get("/", response_model=list[Customer])
async def get_customers(session: SessionDep):
    return session.exec(select(Customer)).all()


@router.get("/{customer_id}", response_model=Customer)
async def read_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer does not exist"
        )
    return customer_db


@router.patch(
        "/{customer_id}",
        response_model=Customer,
        status_code=status.HTTP_200_OK
)
async def update_customer(
        customer_id: int,
        customer_data: CustomerUpdate,
        session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer does not exist"
        )
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db


@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer does not exist"
        )
    session.delete(customer_db)
    session.commit()
    return {"detail": "Customer deleted successfully"}


@router.post('/{customer_id}/plans/{plan_id}')
async def subscribe_customer_to_plan(
    customer_id: int,
    plan_id: int,
    session: SessionDep,
    plan_status: StatusEnum = Query()
):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)

    if not customer_db or not plan_db:
        raise HTTPException(
            status_code=404,
            detail="Customer or Plan not found"
        )

    customer_plan_db = CustomerPlan(
        plan_id=plan_db.id,
        customer_id=customer_db.id,
        status=plan_status
    )
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)

    return customer_plan_db


@router.get('/{customer_id}/plans', tags=["Plans"])
async def get_customer_plans(
    customer_id: int,
    session: SessionDep,
    plant_status: StatusEnum = Query()
):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    query = select(CustomerPlan).where(
        CustomerPlan.customer_id == customer_id,
        CustomerPlan.status == plant_status
    ).where(CustomerPlan.status == plant_status)
    plans = session.exec(query).all()
    return plans
