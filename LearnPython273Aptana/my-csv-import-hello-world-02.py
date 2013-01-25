import csv

with open('dowjonesCompanyNames.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('dowjonesCompanyNamesNew.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {'company':rows[0] for rows in reader}
print mydict
		