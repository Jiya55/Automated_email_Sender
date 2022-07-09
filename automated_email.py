#'''
import smtplib
import ssl
from email.message import EmailMessage
import datetime as dt 
from datetime import *
import time
#'''
'''
my email_password= 'wfsjwlldzerhlgtm'
mom email_password = 'ljfbkbmccxjnzcfw'
'''
#'''
def email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, sending_time = None):
    email_creator = EmailMessage()
    email_creator['From'] = email_sender
    email_creator['To'] = email_receiver
    email_creator['Subject'] = subject
    email_creator.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_sender_password)
        if sending_time != None:
            send_time = datetime.strptime(sending_time,  '%b %d %Y %I:%M%p') # set your sending time in UTC
            time.sleep(send_time.timestamp() - time.time())
            smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
            print('email sent')
        else:
            smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
            print('email sent')
def main():
    print('Hello, Welcome to auto mail')
    time.sleep(1)
    print('Please answer the following questions to send an auto mail:')
    time.sleep(1)
    email_sender=input('sender: ')
    print('Jiya:wfsjwlldzerhlgtm; Sonia:ljfbkbmccxjnzcfw')
    email_sender_password=input('app password: ')
    email_receiver = input('Reciver gmail: ')
    subject= input('subject: ') 
    body= input('body: ')
    specific_time= input('any specific date/time to send the email?(yes or no) ')
    if specific_time.lower()=='yes':
        set_time = input('date/time(format=Jun 24 2022 5:36PM): ')
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, set_time)
    else:
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body)
main()
#'''
'''
scedule mail,
list of ids

import smtplib
import ssl
from email.message import EmailMessage
import datetime as dt 
from datetime import *
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

msg = MIMEMultipart()
msg.attach(MIMEText(file("h.jpg").read()))
msg.attach(MIMEImage(file("CHEAT SHEET.docx").read()))

'''
'''
my email_password= 'wfsjwlldzerhlgtm'
mom email_password = 'ljfbkbmccxjnzcfw'
'''
'''
def email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, sending_time = None):
    
    email_creator = EmailMessage()
    email_creator['From'] = email_sender
    email_creator['To'] = email_receiver
    email_creator['Subject'] = subject
    email_creator.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_sender_password)
        if sending_time != None:
            send_time = datetime.strptime(sending_time,  '%b %d %Y %I:%M%p') # set your sending time in UTC
            time.sleep(send_time.timestamp() - time.time())
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            print('email sent')
        else:
            smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
            print('email sent')
def main():
    print('Hello, Welcome to auto mail')
    time.sleep(1)
    print('Please answer the following questions to send an auto mail:')
    time.sleep(1)
    email_sender=input('sender: ')
    print('Jiya:wfsjwlldzerhlgtm; Sonia:ljfbkbmccxjnzcfw')
    email_sender_password=input('app password: ')
    email_receiver = input('Reciver gmail: ')
    subject= input('subject: ') 
    body= input('body: ')
    specific_time= input('any specific date/time to send the email?(yes or no) ')
    if specific_time.lower()=='yes':
        set_time = input('date/time(format=Jun 24 2022 5:36PM): ')
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, set_time)
    else:
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body)
main()
'''
