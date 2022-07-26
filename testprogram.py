#this child branch contain the codes for python script to automate email message 
#define variables 
MY_ADDRESS = "email@address.com"         # Replace with yours
MY_PASSWORD = "superSecretPassword"      # Replace with yours
RECIPIENT_ADDRESS = "email@address.com"  # Replace with yours

HOST_ADDRESS = 'smtp.host_address.com'   # Replace with yours
HOST_PORT = 587                          # Replace with yours
#sending and email without attachment code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Connection with the server
server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)

# Creation of the MIMEMultipart Object
message = MIMEMultipart()

# Setup of MIMEMultipart Object Header
message['From'] = MY_ADDRESS
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Automated Email"

# Creation of a MIMEText Part
textPart = MIMEText("This is my first plain text automated email\n\nAlessio", 'plain')

# Part attachment
message.attach(textPart)

# Send Email and close connection
server.send_message(message)
server.quit()
