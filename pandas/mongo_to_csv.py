# -*- coding: utf-8 -*-
from pymongo import MongoClient

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize

""" Create a new file in csv format from mongodb database"""

COLLECTION = 'v5'
FILE_ERRORS = 'errores-a-csv-3.txt'
CSV_FILE = '/home/josejm/python-analysis/repositories4.csv'
BUFFER_DOCS = 10 # The bigger, the faster, but could worse repositories

client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']


reposFound = db[COLLECTION].find(projection={'_id': False, 'idioms': True, 'repositoryPath': True})

print "Total" + str(reposFound.count())
listSave = []
num = 0
tot = 0
for repo in reposFound:
    newDoc = {'repository': repo['repositoryPath'],
              'idioms': []}
    for idiomName in repo['idioms']:
        newDoc['idioms'].append({'idiomName': idiomName,
                                 'list': repo['idioms'][idiomName]})
    listSave.append(newDoc)

    num += 1
    if num % BUFFER_DOCS == 0:
        df = json_normalize(listSave, ['idioms', 'list'],['repository', ['idioms', 'idiomName']])
        print num
        tot += df.shape[0]
        print tot
        try:
            df.to_csv(CSV_FILE, mode='a', header=False, index=False)
        except Exception as e:
            print repo['repositoryPath']
            with open(FILE_ERRORS, 'a') as f:
                for r in listSave:
                    f.write(r['repository'].encode('utf-8') + "\n")
                f.write('\n')
        finally:
            listSave = []
