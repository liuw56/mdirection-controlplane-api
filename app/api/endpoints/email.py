from api.models.email import CustomizationRequest
from fastapi import APIRouter, Request
import api.services.email as email
from api.models.email import CustomizationRequest
router = APIRouter(
    prefix="/email",
    tags=["email"]
)

@router.post("/")
def send_customize_email(request: Request,
custimazation: CustomizationRequest
):
    return email.send_customization_email(custimazation)

@router.get("/email")
def read_root(request: Request
):
    return email.get_customization_template()