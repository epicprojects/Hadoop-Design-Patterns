#!/usr/bin/python

import sys
import csv
import heapq, random
import operator


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    mylist = []
    dict = {}
    index = 0
    for line in reader:

        mylist.append(line)
        dict[index] = len(line[4])
        index += 1
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    for i in reversed(sorted_x[0:10]):
        print """\"\"\t\"\"\t\"\"\t\"\"\t\"{0}\"\t\"\"""".format(str(mylist[i[0]][4]))


mapper()
    
