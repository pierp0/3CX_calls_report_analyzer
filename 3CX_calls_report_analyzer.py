import emailAndParser
import logfile
import yaml
import sys
import termcolor
import time
import os


def __getConfig(path='./'):
    with open('./config.yml', 'r') as confFile:
        conf = yaml.safe_load(confFile)
    return conf


if __name__ == "__main__":
    conf = __getConfig()
    if len(sys.argv) == 1:
        print(termcolor.colored("""
        +----------------------------------------+
        |        STARTING 3CX ANALYZER           |
        +----------------------------------------+
        """, 'green'))
        while True:
            path = emailAndParser.downloadEmail(conf['download']['addr'], conf['download']['port'], conf['download']['usr'], conf['download']['pwd'])
            if path:
                lf = logfile.logfile(path)
                emailAndParser.sendEmail(lf.getPDF, conf['send']['addr'], conf['send']['port'], conf['send']['usr'], conf['send']['pwd'], conf['send']['saddr'], conf['send']['raddr'])
                break
            else:
                time.sleep(15)
    elif sys.argv[1] == '-l':
        print(termcolor.colored("""
        +----------------------------------------+
        |        STARTING 3CX ANALYZER           |
        +----------------------------------------+
        """, 'green'))
        fileList = os.listdir('./')
        for file in fileList:
            if '.csv' in file:
                lf = logfile.logfile(os.path.join('./', file))
                emailAndParser.sendEmail(lf.getPDF, conf['send']['addr'], conf['send']['port'], conf['send']['usr'], conf['send']['pwd'], conf['send']['saddr'], conf['send']['raddr'])
    else:
        print(termcolor.colored("""
        +----------------------------------------+
        |               NEED HELP?               |
        +----------------------------------------+
        """, 'green'))
        print("""
        NAME
                3CX_calls_report_analyzer.py
        SYNOPSIS
                3CX_calls_report_analyzer.py [-h]
        DESCRIPTION
            -h  to show this help
            -l  to upload report files from local directory
        MORE INFORMATION AT
            https://github.com/pierp0/3CX_calls_report_analyzer
        """)

# server_address = (conf['server']['ip'], int(conf['server']['port']))
