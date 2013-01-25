import csv
import sys
import profile

def readCSV01():
	#from documentation
	d={}
	with open(sys.argv[1], 'rt') as f:
		reader = csv.DictReader(f)
		for row in reader:
			print row

print 'RAW'
profile.run('print readCSV01(); print')




		






































		