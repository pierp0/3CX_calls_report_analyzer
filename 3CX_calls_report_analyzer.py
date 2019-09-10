import emailAndParser
import logfile
import yaml
import sys
import termcolor
import time

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print(termcolor.colored("""
        +----------------------------------------+
        |        STARTING 3CX ANALYZER           |
        +----------------------------------------+
        """, 'green'))

        with open('./config.yml', 'r') as confFile:
            conf = yaml.safe_load(confFile)
        while True:
            if emailAndParser.downloadEmail(conf['download']['addr'], conf['download']['port'], conf['download']['usr'], conf['download']['pwd']):
                print('QUI')
                # lf = logfile.logfile()
                # emailAndParser.sendEmail(conf['send']['addr'], conf['send']['port'], conf['send']['usr'], conf['send']['pwd'], conf['send']['saddr'], conf['send']['raddr'])
                break
            else:
                time.sleep(15)

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
        MORE INFORMATION AT
            https://github.com/pierp0/3CX_calls_report_analyzer
        """)

# server_address = (conf['server']['ip'], int(conf['server']['port']))
