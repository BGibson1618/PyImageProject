import os
import smtplib
from string import Template
from pathlib import Path
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()
MY_ADDRESS = os.getenv('MY_ADDRESS')
MY_PWD = os.getenv('MY_PASSWORD')

html_temp = Template(Path('index.html').read_text())

email1 = EmailMessage()
email1['from'] = 'Brent Gibson'
email1['to'] = 'bgibson1618@gmail.com'
email1['subject'] = 'You Win!'

email1.set_content(html_temp.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(MY_ADDRESS, MY_PWD)
    smtp.send_message(email1)
