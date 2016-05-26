import pythonic as pyth
import os
import re
from collections import defaultdict
import operator


def isPythonFile(filepath):
    """
    Is the path passed a Python file?
    """
    isPython = False
    # Commonly files found in repositories and aren't python code
    OMIT_FILES = ['README', 'LICENSE', 'NOTICE', 'HEAD', 'DETAILS', 'BUILD', 'DEPENDS', '.gitignore']
    (root, ext) = os.path.splitext(filepath)
    if root.split('/')[-1] not in OMIT_FILES and not re.search('\/.git\/', root):
        if ext == '.py':
            isPython = True
        elif ext == '':
            with open(filepath, 'r') as file:
                isPython = bool(re.search('#!.*python', file.readline()))
    return isPython

def getPyfilesIn(path):
    """
    Look for python files in repository and returns a list of them
    """
    filesList = []
    for root, dirs, files in os.walk(path):
        for name in files:
            filepath = os.path.join(root, name)
            if not os.path.islink(filepath) and isPythonFile(filepath):
                filesList.append(filepath)
    return filesList


def getMethodsInRepo(repoPath):
    dictMethods = defaultdict(int)
    dictMethodsTot = defaultdict(int)

    for pythonfile in getPyfilesIn(repoPath):
        with open(pythonfile, 'rt') as file:
            code = file.read()
        for method in pyth.findMagicMethods(code):
            dictMethods[method] = 1
            dictMethodsTot[method] += 1
    return (dictMethods, dictMethodsTot)

if __name__ == '__main__':
    MAIN_PATH = '/media/josejm/HDD/PYTHON/2/code-repos'
    allMethodsDict = defaultdict(int)
    allMethodsDictTot = defaultdict(int)
    i = 0
    # Each repository is inside a directory, inside the main directory
    for entry in os.listdir(MAIN_PATH):
        entryPath = os.path.join(MAIN_PATH, entry)
        if os.path.isdir(entryPath):
            i+=1
            # there should be only a directory containing the repository
	    try:
                repoName = os.listdir(entryPath)[0]
                repoPath = os.path.join(entryPath, repoName)
                (dictMethods, dictMethodsTot) = getMethodsInRepo(repoPath)
                for (key, value) in dictMethods.items():
                    allMethodsDict[key] += value
                for (key, value) in dictMethodsTot.items():
                    allMethodsDictTot[key] += value
	    except Exception as e:
		print e
		print entryPath
	        print "......................................................................................"

            if i%10 == 0:
                print i
            if i%100 == 0:
                print sorted(allMethodsDict.items(), key=operator.itemgetter(1))
                print "*--*--*--*--*--*--*--*--*--*--*--*--*--*--*"
                print sorted(allMethodsDictTot.items(), key=operator.itemgetter(1))
