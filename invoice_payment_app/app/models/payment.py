from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    reference_no = Column(String(100), nullable=False)
    method = Column(String(50), nullable=False)

    invoice = relationship("Invoice", back_populates="payments")
