from sys import argv
import pandas as pd

### Example Command Usage
#
#   $ python3 csv-combiner.py accessories.csv clothing.csv > combined.csv
#
#   This takes the contents of accessories.csv and clothing.csv
#   and outputs them (with an additional column of filename) 
#   to the new file combined.csv

headers = "email_hash, category, filename"
print(headers)

for i in range(1,len(argv)):
	file = pd.read_csv(argv[i])
	file['filename'] = argv[i]

	for j in range(len(file.index)):
		row = ""
		for k in range(len(file.columns)):
			new = file.iloc[j,k]
			new += ", "
			row += new
		row = row[:-2]
		print(row)			
