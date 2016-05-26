import shutil
import os
import sys


os.chdir("/home/josejm/python-analysis/")

THREAD_FOLDER = "threads"


# FROM CODE REPOS TO THREAD
def a():
    listFiles = os.listdir('code-repos')
    index = 0
    for file in listFiles:
        if index % 500 == 0:
            name = THREAD_FOLDER + '/' + str(index/500)
            os.mkdir(name)
        shutil.move('code-repos/' + file, name)
        index += 1

# FROM THREAD TO CODE REPOS
def b():
    director = THREAD_FOLDER + "/" + sys.argv[1]
    listFiles = os.listdir(director)
    index = 0
    for file in listFiles:
        shutil.move(director + "/" + file, 'code-repos')
        index += 1
        print index

#ADDITIONAL FUNCTION
def c():
    count = 0
    for item in os.listdir('threads/1'):
        count += 1
        print count
        shutil.move('threads/1/' + item, 'threads/0/')
        if count > 60:
            break
c()
