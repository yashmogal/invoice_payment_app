from sqlalchemy.orm import Session
from app.models.invoice import Invoice
from app.models.payment import Payment

def reconcile_payments(db: Session):
    results = []
    invoices = db.query(Invoice).all()
    for invoice in invoices:
        payments = db.query(Payment).filter(Payment.invoice_id == invoice.id).all()
        total_paid = sum([p.amount for p in payments])
        discrepancy = round(invoice.amount - total_paid, 2)

        results.append({
            "invoice_id": invoice.id,
            "invoice_number": invoice.invoice_number,
            "invoice_amount": invoice.amount,
            "total_paid": total_paid,
            "discrepancy": discrepancy,
            "status": "MATCHED" if discrepancy == 0 else "MISMATCHED"
        })
    return results
