from fastapi import APIRouter
from . import invoice

api_router = APIRouter()
api_router.include_router(invoice.router, prefix="/api/v1", tags=["Invoice"])
