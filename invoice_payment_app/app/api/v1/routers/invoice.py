from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceResponse
from app.core.database import get_db

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=InvoiceResponse)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    existing = db.query(Invoice).filter(Invoice.invoice_number == invoice.invoice_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Invoice number already exists")

    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@router.get("/{invoice_number}", response_model=InvoiceResponse)
def get_invoice(invoice_number: str, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.invoice_number == invoice_number).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice
