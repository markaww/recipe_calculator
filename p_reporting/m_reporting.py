from p_acquire.m_acquire import get_recipes
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
email = os.getenv('EMAIL')
pwd = os.getenv('PASSWORD')
destination = os.getenv('DESTINATION')
picks = get_recipes()


def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, pwd)

        subject = 'Your recipe picks for this week'
        body = f"""'Hi! here are your recipe picks for this week.
    {picks} 
    This message was made entirely using python"""

        msg = f'Subject: {subject}\n\n{body}'
        send = smtp.sendmail(email, destination, msg)

        return send



