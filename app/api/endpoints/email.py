from api.models.email import CustomizationRequest, ContactUs
from fastapi import APIRouter, Request
import api.services.email as email
from api.models.email import CustomizationRequest
router = APIRouter(
    prefix="/email",
    tags=["email"]
)

@router.post("/customization")
def send_customize_email(request: Request,
custimazation: CustomizationRequest
):
    return email.send_customization_email(custimazation)

@router.post("/contact-us")
def read_root(request: Request,
contactUs: ContactUs

):
    return email.send_contact_us_email(contactUs)