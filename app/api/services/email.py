import smtplib, ssl
import os, json
from fastapi.templating import Jinja2Templates
from fastapi import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

templates = Jinja2Templates(directory="templates")

def send_email(template):
    sender_email = os.environ.get("SENDER_EMAIL")
    receiver_email = json.loads(os.environ.get("RECEIVER_EMAIL"))
    password = os.environ.get("EMAIL_PW")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "TEST"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.attach(MIMEText(template, 'html'))

    message = """\
    Subject: Hi there

    This message is sent from Python."""
    print(sender_email)
    print(receiver_email)
    port = 465  # For SSL
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def get_customization_template(request: Request, id: id):
    
    return templates.TemplateResponse.render("customization_template.html", { "request": request, "id": id})