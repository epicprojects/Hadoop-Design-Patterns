#!/usr/bin/python

# Import relevant modules
import sys
import csv

# Create a writer object
writer = csv.writer(sys.stdout, delimiter='\t')

# Initialize the keys
key_A = None
key_B = None

# For every line in the standard input...
for line in sys.stdin:
    data = line.strip().split('\t')

    if data[1] == 'A':
		key_A = data[0]
		data_A = data[2:]

    elif data[1] == 'B':
		key_B = data[0]
		data_B = data[2:]

    if key_A == key_B:
        writer.writerow(data_B[:3] + [key_A] + data_B[3:] + data_A)