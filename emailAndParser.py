import imaplib
import smtplib
import urllib.request
import base64


def downloadFile(data):
    linkIndex = data.find('here')
    link = ''
    urllib.request.urlretrieve(link, 'newdata.txt')


def sendEmail(srvaddr='', port=25, usr='', pwd='', saddr='', raddr=''):
    try:
        server = smtplib.SMTP(srvaddr, port)
        server.login(usr, pwd)
        msg = 'this is a test'
        server.sendmail(saddr, raddr, msg)
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
            print data
            downloadFile(data)
            num1 = base64.b64decode(num)
            data1 = base64.b64decode(data[0][1])
            print('MESSAGE %s\n%s\n' % (num1, data1))

        email.close()
        email.logout()
        return True
    except Exception:
        return False

# sendEmail()
