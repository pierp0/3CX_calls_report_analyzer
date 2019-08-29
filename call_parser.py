
import os
from logfile import logfile

fileList = os.listdir('./')
for file in fileList:
    if 'LogChiamateLastWeek' in file: 
        # with open(os.path.join('./', file), 'r') as actualFilePtr:
        actualFile = logfile(os.path.join('./', file))
        actualFileConent = actualFile.getContent()
        for p in actualFileConent:
            print(p + '\n')#str(actualFileConent).split("\n"))

# load conf file yaml
# schedule every monday
# 	Connect to email box
#	download email and get link of the week
#	dowload the  log file
#	analize file
#		number of total calls
#		number of answered phone calls
#		number of missed phone calls
#		number of answered calls per operator (oper code)
#	build a graphic of datas
#	send an email to list-mail-address 