from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentOut

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentOut)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@router.get("/", response_model=list[PaymentOut])
def get_all_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()

@router.get("/{payment_id}", response_model=PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(payment)
    db.commit()
    return {"detail": "Deleted successfully"}
