from fastapi import APIRouter, Request
from api.services.email import get_customization_template, send_email

router = APIRouter(
    prefix="/email",
    tags=["email"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}")
def read_root(request: Request, id: str):
    template = get_customization_template(request, id)
    return send_email(template)