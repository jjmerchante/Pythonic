from pymongo import MongoClient
import os
import sys
import shutil

output = open('output.txt', 'w')


os.chdir('/home/josejm/python-analysis')

client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']

list = db.v3.find({}, {'repositoryPath': True})

index = 0
print list.count()
for repo in list:
    #print os.path.exists('code-repos-done/' + repo['repositoryPath'])
    try:
        shutil.move('code-repos-done/' + repo['repositoryPath'], 'code-repos')
    except Exception as e:
        print "error: " + str(e)
        output.write("error: " + str(e) + "\n")
    index += 1
    print index
