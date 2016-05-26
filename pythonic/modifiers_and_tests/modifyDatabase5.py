from pymongo import MongoClient
import os
import sys
import shutil


client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']

list = db.v4.find()
index = 0
for repo in list:
    index += 1
    if index % 1000 == 0:
        print index
    db.v5.insert(repo)
    """
    if not db.v4.find_one({'repositoryPath': repo['repositoryPath']}):
        db.v4.insert(repo)
    else:
        with open('justDone.txt', 'a') as ff:
            ff.write(repo['repositoryPath'] + "\n")
    """
