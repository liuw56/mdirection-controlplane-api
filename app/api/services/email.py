import html
from api.models.email import ContactUs, CustomizationRequest
from jinja2 import Environment, PackageLoader, select_autoescape
import smtplib, ssl
import os, json
from fastapi.templating import Jinja2Templates
from fastapi import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

templates = Jinja2Templates(directory="templates")

env = Environment(
    loader=PackageLoader('api', 'templates'),
    autoescape=select_autoescape(['html'])
)

def send_email(template, subject):
    print(os.environ.get("SENDER_EMAIL"))
    print(os.environ.get("RECEIVER_EMAIL"))
    sender_email = os.environ.get("SENDER_EMAIL")
    receiver_email = json.loads(os.environ.get("RECEIVER_EMAIL"))
    password = os.environ.get("EMAIL_PW")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = str(receiver_email)
    msg.attach(MIMEText(template, 'html'))

    print(sender_email)
    print(receiver_email)
    port = 465  # For SSL
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # server.sendmail(sender_email,  receiver_email, template)
        # server.send()
        server.sendmail(sender_email, receiver_email, msg.as_string())

def send_customization_email(data: CustomizationRequest):
    template = env.get_template('customization_template.html')
    body:str = template.render(fullName=data.fullName, email=data.email, data = data.items)
    send_email(body, "Customization Request")
    return 

def send_contact_us_email(data: ContactUs):
    template = env.get_template('contact_us_template.html')
    body:str = template.render(fullName=data.fullName, email=data.email, message=data.message)
    send_email(body, "You have received a New Message")
    return 