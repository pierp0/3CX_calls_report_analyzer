
import os
from dateutil.parser import parse

def isDate(stringToAnalyze):
    try:
        parse(stringToAnalyze, fuzzy=True)
        return True
    except Exception as e:
        return False


def restructurizeFile(actualFileConent):
    restructuratedFile = actualFileConent[6:-2]
    for raw in restructuratedFile :
        # if raw start with date get result frome store to restruct and put raw in store
        print raw[:8]
        if isDate(raw[:8]):
            print('OK')
        else: 
            print('KO')
        # else attach raw to last stored raw 
        # 

    return restructuratedFile
    

fileList = os.listdir('./')
for file in fileList:
    if 'LogChiamateLastWeek' in file: 
        with open(os.path.join('./', file), 'r') as actualFilePtr:
            actualFileConent = restructurizeFile(actualFilePtr.readlines())
            # print(actualFileConent)#str(actualFileConent).split("\n"))