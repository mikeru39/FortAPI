import os
import smtplib


SENDER_EMAIL = ''
recipient_email = ''
file_path = 'file.csv'
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = SENDER_EMAIL
msg['To'] = recipient_email
msg.set_content(content)
file_path = os.path.join(file_path)
with open(file_path, 'rb') as f:
    file_data = f.read()
msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_path)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(SENDER_EMAIL, APP_PASSWORD)
    smtp.send_message(msg)
