# -*- coding: utf-8 -*-
from pymongo import MongoClient

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize



client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']

total = 0
max = db.v4.find().count()
found = 0
totalOut = 0
for doc in db.v4.find():
    total += 1
    #print "-----" + doc['repositoryPath'] + "--------------"
    stop = False
    inside = False
    try:
        doc['idioms']['idiomMethods1']
        doc['idioms']['idiomMethods2']
        doc['idioms']['idiomMethods3']
    except:
        with open('/home/josejm/a.txt', 'a') as f:
            f.write(doc['repositoryPath'] + '\n')
        continue
    for idiom in doc['idioms']['idiomMethods1']:
        inside = True
        if not 'method' in idiom:
            found += 1
            stop = True
    if not stop:
        for idiom in doc['idioms']['idiomMethods2']:
            inside = True
            if not 'method' in idiom:
                found += 1
                stop = True
    if not stop:
        for idiom in doc['idioms']['idiomMethods3']:
            inside = True
            if not 'method' in idiom:
                found += 1
                stop = True
    if not inside:
        totalOut += 1
    if stop or not inside:
        print db.v4.remove({'repositoryPath': doc['repositoryPath']})

    print str(total) + "/" + str(max) + " - " +str(found) + " - " +str(totalOut)
