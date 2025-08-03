from fastapi import APIRouter
from db import SessionDep
from models import Plan


router = APIRouter(prefix="/plans", tags=["Plans"])


@router.post("/")
async def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db
