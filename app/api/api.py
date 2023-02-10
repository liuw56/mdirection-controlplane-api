from api.endpoints import email
from api.endpoints import fireStore
from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

router.include_router(email.router)
router.include_router(fireStore.router)