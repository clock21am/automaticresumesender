#!/usr/bin/env python3

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddress = "rajdeep.kaur2009@gmail.com"

print "enter the email address of the HR or the employee who you want to send your resume"

toaddress = raw_input();

