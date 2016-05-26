from collections import namedtuple
import csv
import os

ProjectRecord = namedtuple('ProjectRecord', 'id, url, owner_id, name, descriptor, language, created_at, forked_from, deleted, updated_at')

list = []

esta = 0
noesta = 0
tot = 0

for root, dirs, files in os.walk('json-repos'):
    for file in files:
        list.append(int(file.split('-')[0]))

f1 = 'projects-python_next.csv'
f2 = 'a.csv'

with open(f2, 'r') as csvinput:
    for contents in csv.reader(csvinput, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\"):
        tot+=1
        row = ProjectRecord(*contents)
        if int(row.id) not in list:
            if esta > 0:
                print "si:" + str(esta)
            noesta += 1
            esta = 0
            #print int(row.id)
        else:
            if noesta > 0:
                print "no:" + str(noesta)
            #print "Esta"
            esta+= 1
            noesta = 0
if noesta > 0: print "no:" + str(noesta)
if esta > 0: print "si:" + str(esta)


print "total:" + str(tot)
