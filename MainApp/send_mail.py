# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from .models import Notifications
# import os
# from django.core.mail import send_mail

# def sendmail(event, user):
#     sender_email = os.environ.get("EMAIL_USERNAME")
#     receiver_email = user.email
#     password = os.environ.get("EMAIL_PASSWORD")
#     # Create the plain-text and HTML version of your message
#     text = """\
#     Hi,
#     How are you?
#     Real Python has many great tutorials:
#     www.realpython.com"""
#     html = f"""\
#     <html>
#     <body>
#         <div style="width:80%; margin: auto;">
#             <h1>{event.title} </h1>
#             <p>{event.content} </p>
#             <p>Are you coming?</p>
#             <a href="https://bixert.xyz/verify/{event.id}-{user.id}"><button>Yes</button></a> <button>No</button>
#         </div>
#     </body>
#     </html>
#     """
#     message_body = html
#     send_mail(
#             "Verify Email", #subject
#             message_body, #message
#             sender_email, #from email
#             [receiver_email], #to email
#     )