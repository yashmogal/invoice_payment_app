from pydantic import BaseModel
from datetime import date

class PaymentBase(BaseModel):
    invoice_id: int
    amount: float  # <-- ✅ must match your DB model
    payment_date: date
    reference_no: str
    method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int

    class Config:
        orm_mode = True
