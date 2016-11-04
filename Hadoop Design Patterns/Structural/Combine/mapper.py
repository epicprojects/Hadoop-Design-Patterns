#!/usr/bin/python

# Import relevant modules
import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t')

# Skip the header...
reader.next()

# For every line in the data...
for line in csv.reader(sys.stdin, delimiter='\t'):
    if len(line) == 5:   
	    writer.writerow([line[0]] + ['A'] + line[1:])

    elif len(line) == 19:
	    writer.writerow([line[3]] + ['B'] + line[:3] + line[5:10])