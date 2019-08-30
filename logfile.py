from dateutil.parser import parse
from datetime import datetime as dt
import pandas as pd


class logfile():

	def __init__(self, fp):
		#self.basefile = actualFile
		self.dfFile = pd.read_csv(fp, engine = 'python', header = 5, skipfooter = 2, usecols = ["Tempo della Chimata", "Caller ID", "Destinazione", "Stato", "Squillo", "Conversazione", "Totale", "Motivo"])
		self._contentFile = ''
		#self._restructurizeFile()
		self._week = 0
		self._totcalls = 0
		self._missedcalls = 0
		# Operators{'internal_number_0': 'operator_name_0', ... , 'internal_number_n': 'operator_name_n'} numb of answered calls
		self._operators = {}
		self._analyzeLog(fp)



	def _analyzeLog(self, fp):
		with open(fp, 'r') as file:
			# Select the 3th row and get a substr with the start date
			next(file)
			next(file)
			# Convert substr into a date and use it to get the week number
			data = dt.strptime(file.readline()[24:-29].strip(), '%d/%m/%y')
		self._week = dt.date(data).isocalendar()[1]
		dfFileNotNull = self.dfFile['Tempo della Chimata'].notnull()
		self._totcalls = self.dfFile['Tempo della Chimata'].count()
		# self._missedcalls = 0
		# self._operators
		

	def _isDate(self, stringToAnalyze):
	    try:
	        parse(stringToAnalyze, fuzzy=True)
	        return True
	    except Exception as e:
	        return False

	def _restructurizeFile(self):
	    restructuratedFile = []
	    storage = None
	    actualFileConent = (self.basefile.readlines())[6:-2]
	    for raw in actualFileConent :
	        # if raw start with date get result frome store to restruct and put raw in store
	        if self._isDate(raw[:8]):
	            if storage is not None:
	                restructuratedFile.append(storage)
	            storage = raw 
	        else: 
	            storage += raw
	    self._contentFile = restructuratedFile

	def _setWeek():
		pass

	def _setTotCalls():
		pass

	# def analizeFile(self):
	# 	self.setWeek()
	# 	self.setTotCalls()

	def getContent(self):
		return self._contentFile

	def getTotCalls(self):
		return self._totcalls

	def getWeek(self):
		return self._week

	def getMissedCalls(self):
		return self._missedcalls