import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']
print "reading..."
df = pd.read_csv('/home/josejm/python-analysis/repositories3.csv', names=['author', 'file', 'lineNum', 'method', 'idiom', 'repository'])
print "begin"
num = 0
deleted = 0
print len(df['idiom'].unique())
"""for repo in df['idiom'].unique():
    num += 1
    result = db.v5.delete_many({'repositoryPath': repo})
    deleted += result.deleted_count
    print num, deleted"""
