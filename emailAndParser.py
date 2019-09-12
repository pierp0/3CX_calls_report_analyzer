import imaplib
import smtplib
# import email
import urllib3.request
# import base64
import re
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def downloadFile(data):
    # https://tgs.my3cx.it:5001/management/Reports/LogChiamateSettimanale_0209_fiK9AQZJ4vvLaYAXITvb.csv
    test = re.search("https\:\/\/.{1,20}\.my3cx\.it\:5001\/management\/Reports\/.{1,30}_[0-9]{4}_[a-zA-Z0-9]{20}.csv", str(data)).group()
    nameFile = os.basename(test)
    urllib.request.urlretrieve(test, nameFile)
    return os.path.join('./', nameFile)


def sendEmail(attachpath, srvaddr='', port=25, usr='', pwd='', saddr='', raddr=''):

    subject = "3CX Weekly report"
    body = "3CX Weekly report"
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = saddr
    message["To"] = raddr
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    with open(attachpath, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    try:
        server = smtplib.SMTP(srvaddr, port)
        server.login(usr, pwd)
        server.sendmail(saddr, raddr, text)
        server.close()
    except Exception as e:
        raise e


def downloadEmail(srvaddr='', port='', usr='', pwd=''):
    try:
        email = imaplib.IMAP4_SSL(srvaddr, port)
        email.login(usr, pwd)
        email.select()
        typ, data = email.search(None, '(UNSEEN)')

        for num in data[0].split():
            typ, data = email.fetch(num, '(RFC822)')
            print(data)
            path = downloadFile(data)
            # num1 = base64.b64decode(num)
            # data1 = base64.b64decode(data[0][1])
            # print('MESSAGE %s\n%s\n' % (num1, data1))

        email.close()
        email.logout()
        return path
    except Exception:
        print('ERRORE')
        return False

# sendEmail()
