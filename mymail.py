import email
import getpass
import os
import smtplib
import ssl

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmymail(srvaddr, sender, reciver_lst, passwd=None, port=465, sbj='', body='', attachpath_lst=None):
    if passwd is None:
        passwd = getpass.getpass('Give me your passwd:')

    if isinstance(reciver_lst, str):
        reclst = []
        reclst.append(reciver_lst)
        reciver_lst = reclst
        # list(reciver_lst).append(reciver_lst)

    if isinstance(attachpath_lst, str):
        att_lst = []
        att_lst.append(attachpath_lst)
        attachpath_lst = att_lst
        # list(attachpath_lst).append(attachpath_lst)

    message = MIMEMultipart()
    message["Subject"] = sbj
    message["From"] = sender
    message["To"] = ", ".join(reciver_lst)
    message.attach(MIMEText(body, 'plain'))

    if attachpath_lst:
        for path in attachpath_lst:
            filename_lst = os.path.basename(path)
            part = MIMEBase('application', 'octet-stream')

            try:
                part.set_payload(open(path, 'rb').read())
            except Exception as e:
                raise e

            email.encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename_lst}",
            )
            message.attach(part)

    text = message.as_string()
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(srvaddr, port, context=context) as server:
            server.login(sender, passwd)
            server.sendmail(sender, reciver_lst, text)
    except Exception as e:
        raise e
