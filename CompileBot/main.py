import os
import time

import imaplib
import email
import sys
import traceback

from smtplib import SMTP_SSL, SMTP_SSL_PORT

username = os.environ['username']
password = os.environ['password']

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)

SMTP_HOST = 'smtp.gmail.com'
SMTP_USER = os.environ['username']
SMTP_PASS = os.environ['password']

def sendEmail(boolSuccess, body, Abody):

    if boolSuccess == True:
        extra = """
        The running of this script went off without a hitch.

        Runtime output:
        """
        title = "Successful Compile Action"
    else:
        extra = """
        This script encountered an error.

        Output and fullstack information:
        """
        title = "Compile Action Error"

    if Abody:
        body = extra+str(Abody)+str(body)
    else:
        body = extra+str(body)
    subject = title
    from_email = "Compile Bot"
    to_emails = [os.environ("SendAddress")]
    headers = f"From: {'CompileBot'}\r\n"
    headers += f"To: {', '.join(to_emails)}\r\n" 
    headers += f"Subject: "+subject+"\r\n"
    email_message = headers + "\r\n" + body

    smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
    smtp_server.set_debuglevel(1)
    smtp_server.login(SMTP_USER, SMTP_PASS)
    smtp_server.sendmail(from_email, to_emails, email_message)

    return

class InterpreterError(Exception): pass

def my_exec(cmd, globals=None, locals=None, description='source string'):

    try:
        exec(cmd, globals, locals)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        with open("MainOutput.txt", 'r') as f:
         return [None, f.read()]

    with open("MainOutput.txt", 'r') as f:
     return [InterpreterError("%s at line %d of %s: %s" % (error_class, line_number, description, detail))]

    with open("MainOutput.txt", 'r') as f:
     return [None, f.read()]

def grabEmail():

  status, messages = imap.select("INBOX")

  messages = int(messages[0])

  result, data = imap.uid('search', None, "UNSEEN")
  i = len(data[0].split())

  for x in range(i):

    outputFile = open("MainOutput.txt", "a+")
    outputFile.truncate(0)
    outputFile.close()

    latest_email_uid = data[0].split()[x]
    result, email_data = imap.uid('fetch', latest_email_uid, '(RFC822)')
    
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

    if "CompileCode" in subject:
      
      a = str(email_message)

      if os.environ("SendName") in email_from:
       b = a.split("Content-Type: text/plain; charset=\"UTF-8\"")[1]
       c = b.split("--")[0]
       executable = my_exec(c)

       if executable[0] == None:
           sendEmail(True, open("MainOutput.txt", "r").read(), None)
       else:
           sendEmail(False, executable, open("MainOutput.txt", "r").read())

       return
    return subject
  return

while true do
    grabEmail()
    time.sleep(1)

imap.close()
imap.logout()    
