import imaplib
# import email
import urllib3.request
# import base64
import re
import os
import mymail


def downloadFile(data):
    test = re.search(
            "https\:\/\/.{1,20}\.my3cx\.it\:5001\/management\/Reports\/.{1,30}_[0-9]{4}_[a-zA-Z0-9]{20}.csv",
            str(data)
    ).group()
    nameFile = os.basename(test)
    urllib3.request.urlretrieve(test, nameFile)
    return os.path.join('./', nameFile)


def sendEmail(attachpath, srvaddr='', port=25, usr='', pwd='', saddr='', raddr=''):

    sbj = "3CX Weekly report"
    body = "3CX Weekly report"

    mymail.sendmymail(srvaddr, saddr, raddr, pwd, port, sbj, body, attachpath)


def downloadEmail(srvaddr='', port='', usr='', pwd=''):
    try:
        mymail = imaplib.IMAP4_SSL(srvaddr, port)
        mymail.login(usr, pwd)
        mymail.select()
        typ, data = mymail.search(None, '(UNSEEN)')

        for num in data[0].split():
            typ, data = mymail.fetch(num, '(RFC822)')
            path = downloadFile(data)
            # num1 = base64.b64decode(num)
            # data1 = base64.b64decode(data[0][1])
            # print('MESSAGE %s\n%s\n' % (num1, data1))

        mymail.close()
        mymail.logout()
        return path
    except Exception:
        print('ERRORE')
        return False

# sendEmail()
