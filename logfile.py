from dateutil.parser import parse

class logfile():

	def __init__(self, actualFile):
		self.basefile = actualFile
		self.__contentFile = ''

	def isDate(self, stringToAnalyze):
	    try:
	        parse(stringToAnalyze, fuzzy=True)
	        return True
	    except Exception as e:
	        return False

	def restructurizeFile(self):
	    restructuratedFile = []
	    storage = None
	    actualFileConent = (self.basefile.readlines())[6:-2]
	    for raw in actualFileConent :
	        # if raw start with date get result frome store to restruct and put raw in store
	        if self.isDate(raw[:8]):
	            if storage is not None:
	                restructuratedFile.append(storage)
	            storage = raw 
	        else: 
	            storage += raw
	    self.__contentFile = restructuratedFile

	def getContent(self):
		return self.__contentFile