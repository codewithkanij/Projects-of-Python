# This is the new way of sanding a mail with Pyton because as i said the old way is no more working basically
# so what we need to do now is to adapt to this new way

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'kanijsworna29@gmail.com'
email_password = 'ozpdvimzpzhxzknj '

email_receiver = 'petapa1519@dmonies.com'        # temporary email-address
subject = "Don't forgate to subscribe"
body = """
When you watch a video, Please subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email successfully sent.")
