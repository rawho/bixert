import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import Notifications

def sendmail(event, user):
    sender_email = "bixertbot@gmail.com"
    receiver_email = "adi@cet.ac.in"
    password = "Bixert@123"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Invitation"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = f"""\
    <html>
    <body>
        <div style="width:80%; margin: auto;">
            <h1>{event.title} </h1>
            <p>{event.content} </p>
            <p>Are you coming?</p>
            <a href="http://127.0.0.1:8000/verify/{event.id}-{user.id}"><button>Yes</button></a> <button>No</button>
        </div>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    Notifications.objects.create(user = user,notification = f"Please confirm your invitation for {event.title} sent to your mail {user.email}")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
