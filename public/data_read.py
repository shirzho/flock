import csv

def readcsv(filename):	
	ifile = open(filename, "rU")
	reader = csv.reader(ifile, delimiter=";")

	rownum = 0	
	a = []

	for row in reader:
		temp = [0,0]
		count = 0
		for x in row[0].split(','):
			if(count == 1):
				temp[0] = float(x)
			if(count == 0):
				temp[1] = float(x)
			count += 1
		if(temp[1] != 0 and temp[0] != 0):
			a.append(temp)
		rownum += 1
    
	ifile.close()
	return a

out = readcsv("pitcrime.csv")

with open('crimedataout.txt', 'w') as f:
	count = 0
	for item in out:
		if(count < 1000):
			f.write("%s," % item)
		count += 1
f.close()