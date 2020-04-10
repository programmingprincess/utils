import csv


# Read any file (parse the columns yourself)
def read_file(filename):
	with open(filename) as f:
	  for line in f:
	  	print(f)


# Read comma- or tab-separated files ("delimiter")
# Have to import CSV 
def read_csv(filename):
	with open(filename) as f:
	    reader = csv.reader(f, delimiter=',')
	    for idx, row in enumerate(reader):
	        print(row)
	        print(row[0])