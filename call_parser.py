
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