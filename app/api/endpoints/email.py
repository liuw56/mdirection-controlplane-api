from fastapi import APIRouter, Request
import api.services.email as email

router = APIRouter(
    prefix="/email",
    tags=["email"]
)

@router.get("/{id}")
def read_root(request: Request, id: str):
    template = email.get_customization_template(request, id)
    return email.send_email(template)