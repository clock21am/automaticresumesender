#!/usr/bin/env python3

import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddress = "rajdeep.kaur2009@gmail.com"
print "enter the email address of the HR or the employee who you want to send your resume"
toaddr = raw_input()

subjectofemail = "aspiring to work in xyz company"

messagetobesent = "xxx"

msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddr
msg['Subject'] = subjectofemail
filepath = os.path.dirname(os.path.abspath(__file__))

body = messagetobesent
msg.attach(MIMEText(body,'plain'))

filename = "/Rajdeepkaur_Resume.pdf"
attachment = open(filepath+filename,"rb")

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP(host='smtp.gmail.com',port='587')
server.starttls()
server.login(fromaddr,"password")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()

