import imaplib
import smtplib
# import base64


def parseEmail(data):
    pass


def sendEmail():
    addr = ''
    port = 25
    usr = ''
    pwd = 'test123'
    print('tento creazione server')
    server = smtplib.SMTP(addr, port)
    print('tento connessione')
    server.login(usr, pwd)
    print('login OK')
    msg = 'this is a test'
    server.sendmail('test@gmail.com', 'test@gmail.com', msg)
    print('mail sent')
    server.close()
    # server.logout()


def downloadEmail():
    usr = 'test@gov.it'
    pwd = 'passwd'
    addr = 'add'
    port = '123'

    email = imaplib.IMAP4_SSL(addr, port)
    email.login(usr, pwd)
    email.select()

    typ, data = email.search(None, '(UNSEEN)')

    for num in data[0].split():
        typ, data = email.fetch(num, '(RFC822)')
        parseEmail(data)
        # num1 = base64.b64decode(num)
        # data1 = base64.b64decode(data[0][1])
        # print('MESSAGE %s\n%s\n' % (num, data1))

    email.close()
    email.logout()


sendEmail()
