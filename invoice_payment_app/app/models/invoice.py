from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True, nullable=False)
    customer_name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), default="pending")
    due_date = Column(Date, nullable=False)

    payments = relationship("Payment", back_populates="invoice", cascade="all, delete")
