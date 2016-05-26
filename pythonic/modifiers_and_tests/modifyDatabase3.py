from pymongo import MongoClient
import os
import sys
import shutil


client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']
"""
list = db.v1_1.find({}, {'repositoryPath': True})
index = 0
for repo in list:
    index += 1
    if db.v1.find({'repositoryPath': repo['repositoryPath']}).count() > 1:
        print repo
    else:
        print index
"""

list = db.v1_1.find()
index = 0
for repo in list:
    index += 1
    documentResult = {
                        "repositoryPath": repo['repositoryPath'],
                        "idioms":
                        {
                        	"NestedFunction" : repo["NestedFunction"],
                        	"ifNameMain" : repo["ifNameMain"],
                        	"finally" : repo["finally"],
                        	"generators" : repo["generators"],
                        	"idiomMethods3" : repo["idiomMethods3"],
                        	"idiomMethods2" : repo["idiomMethods2"],
                        	"idiomMethods1" : repo["idiomMethods1"],
                        	"defaultdict" : repo["defaultdict"],
                        	"deque" : repo["deque"],
                        	"namedTuple" : repo["namedTuple"],
                        	"docstring" : repo["docstring"],
                            "assert" : repo["assert"],
                            "equalFunctionCall" : repo["equalFunctionCall"],
                            "with" : repo["with"],
                        	"decorator" : repo["decorator"],
                        	"assignOneLine" : repo["assignOneLine"],
                        	"yield" : repo["yield"],
                        	"listComprehension" : repo["listComprehension"],
                        	"lambda" : repo["lambda"]
                        },
                        "antiidioms": {}
                    }
    if index % 50 == 0:
        print index
    if not db.v2.find_one({'repositoryPath': repo['repositoryPath']}):
        db.v2.insert(documentResult)
    else:
        with open('justDone.txt', 'a') as ff:
            ff.write(repo['repositoryPath'] + "\n")
