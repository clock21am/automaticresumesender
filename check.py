#!/usr/bin/env python3
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "rajdeep.kaur2009@gmail.com"
toaddr = "rajdeep51994@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

 
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login(fromaddr, "rajdeepkaur")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
