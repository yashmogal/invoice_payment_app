from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.reconciliation import reconcile_payments

router = APIRouter(
    prefix="/reconciliation",
    tags=["Reconciliation"]
)

@router.get("/", summary="Get reconciliation report")
def get_reconciliation_report(db: Session = Depends(get_db)):
    return reconcile_payments(db)
