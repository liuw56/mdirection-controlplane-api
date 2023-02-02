from api.endpoints import email
from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

router.include_router(email.router)