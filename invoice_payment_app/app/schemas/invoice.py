from pydantic import BaseModel
from datetime import date

class InvoiceBase(BaseModel):
    invoice_number: str
    customer_name: str
    amount: float
    due_date: date
    status: str = "pending"

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
