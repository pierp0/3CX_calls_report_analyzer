import imaplib
import smtplib
import urllib.request
# import base64
import re


def downloadFile(data):
    print('\nDOWN\n')
    # https://tgs.my3cx.it:5001/management/Reports/LogChiamateSettimanale_0209_fiK9AQZJ4vvLaYAXITvb.csv
    test = re.search("https\:\/\/.{1,20}\.my3cx\.it\:5001\/management\/Reports\/.{1,30}_[0-9]{4}_[a-zA-Z0-9]{20}.csv", str(data)).group()
    print('TEST\n')
    print(test)
    # linkIndex = data.find('here')
    # link = ''
    print('SAVE\n')
    urllib.request.urlretrieve(test, 'newdata.txt')


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
        print('DOWNLOAD EMAIL')
        # print('downloademail')
        email = imaplib.IMAP4_SSL(srvaddr, port)
        # print('login')
        email.login(usr, pwd)
        # print('select')
        email.select()

        typ, data = email.search(None, '(UNSEEN)')
        print('prima di for')
        for num in data[0].split():
            typ, data = email.fetch(num, '(RFC822)')
            print(data)
            downloadFile(data)
            # num1 = base64.b64decode(num)
            # data1 = base64.b64decode(data[0][1])
            # print('MESSAGE %s\n%s\n' % (num1, data1))

        email.close()
        email.logout()
        return True
    except Exception:
        print('ERRORE')
        return False

# sendEmail()
