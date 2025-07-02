from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.routers import api_router
from app.routers import reconciliation, payment
from app.core.database import Base, engine
Base.metadata.create_all(bind=engine)


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Invoice Payment Reconciliation API")

# Register routes
app.include_router(api_router)  # /api/v1/invoices
app.include_router(payment.router)  # /payments
app.include_router(reconciliation.router)  # /reconciliation
