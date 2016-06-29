#!/usr/bin/python
import csv
import sys
from collections import namedtuple

ProjectRecord = namedtuple('ProjectRecord', 'id, url, owner_id, name, descriptor, language, created_at, forked_from, deleted, updated_at')

def filterRow(contents):
    """ 0,2,7 and 8 are integers but QUOTE_NONNUMERIC change it to float,
    7 (forked_from) should be an integer, so I use 0 instead of N
    """
    contents[0] = int(contents[0])
    contents[2] = int(contents[2])
    contents[7] = 0
    contents[8] = int(contents[8])
    return contents


def filterGHTorrentCSV(csvfilein, csvfileout, language=''):
    """Delete the removed repositories from github
    and the repositories that has been forked

    Also allow to filter the main language of the repository
    """
    fout = open(csvfileout, 'w')
    csvoutput = csv.writer(fout, quoting=csv.QUOTE_NONNUMERIC)
    num_lines = sum(1 for line in open(csvfilein, "r"))
    lines_done = 0

    with open(csvfilein, "r") as csvinput:
        for contents in csv.reader(csvinput, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\"):
            row = ProjectRecord(*contents)
            if not row.deleted and row.forked_from == 'N':
                contents = filterRow(contents)
                if not language:
                    csvoutput.writerow(contents)
                elif row.language == language:
                    csvoutput.writerow(contents)
                else:
                    pass
                    #print (row.id, row.deleted, row.forked_from, row.language)
            lines_done += 1
            if lines_done % 100000 == 0:
                print '\r', float(lines_done)/num_lines*100, '%',
                sys.stdout.flush()
        print '\rFINISH!            '
        sys.stdout.flush()
    fout.close()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        inputcsv = sys.argv[1]
        outputcsv= sys.argv[2]
        filterGHTorrentCSV(inputcsv, outputcsv, language='Python')
    else:
        print "usage: python", sys.argv[0], "inputfile outputfile"
