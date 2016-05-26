import csv
import urllib2
import os
import json
import re
from time import sleep
from sys import exit
from collections import namedtuple


ProjectRecord = namedtuple('ProjectRecord', 'id, url, owner_id, name, descriptor, language, created_at, forked_from, deleted, updated_at')
TREES_DIR = 'trees-repos'
PYTH_LISTS_DIR = 'lists-python'
access_token = ''


def log(msg, level=0):
    """
    Print a message with differents levels of importance
    0: trace, 1: info, 2: warn, 3: error
    """
    color = ['\033[0m', '\033[94m', '\033[93m', '\033[91m']
    if level < 0  or level > 3: level = 0
    print color[level] + msg + '\033[0m'


def possiblePython(filename):
    (root, ext) = os.path.splitext(filename)
    return ext == '.py'


def getRepoTree(urlrepo, filename):
    """
    Download the json tree of the repository and return the content
    Also checks if the filename is downloaded. In that case, returns nothing
    """
    if os.path.exists(filename):
        log("{0}: JSON already exists".format(filename), 1)
        #with open(filename, 'r') as data:
        #    jsontree = json.load(data)
        jsontree = ''
    else:
        try:
            urlrepo += '&access_token=' + access_token
            response = urllib2.urlopen(urlrepo)
        except urllib2.URLError as error:
            errorMsg =  "------------ WARNING -------------\n"
            errorMsg += "url: " + urlrepo + '\n'
            errorMsg += "filename: " + filename + '\n'
            errorMsg += "Error: " + str(error) + '\n'
            errorMsg += "----------------------------------"
            log(errorMsg, 3)
            exit(-1)
        jsontree = json.load(response)
        with open(filename, 'w') as fd:
            fd.write(json.dumps(jsontree))
            log("{0}: JSON downloaded and saved".format(filename), 1)
    return jsontree


def findPythonFiles(jsontree, jsonrepo, reponame):
    """ Find potential python files from a json repository tree """

    if jsontree['truncated']:
        log('TRUNCATED TREE -> CLONE: {0}'.format(jsonrepo['clone_url']), 2)
        with open('truncatedTrees.txt', 'a+') as truncatedTreesLog:
            truncatedTreesLog.write(jsonrepo['clone_url'] + '\n')
    else:
        files = []
        for file in jsontree['tree']:
            if file['type'] == 'blob' and possiblePython(file['path']):
                log('Python file: ' + file['path'], 1)
                urlFile = 'https://raw.githubusercontent.com/{0}/{1}/{2}'.format(
                                                                            jsonrepo['full_name'],
                                                                            jsonrepo['default_branch'],
                                                                            file['path'])
                files.append(urlFile)
        with open(PYTH_LISTS_DIR +"/"+ reponame, 'w') as fileList:
            fileList.write('\n'.join(files))


def getPythonFiles():
    if not os.path.exists(TREES_DIR):
        os.mkdir(TREES_DIR)
    if not os.path.exists(PYTH_LISTS_DIR):
        os.mkdir(PYTH_LISTS_DIR)

    list = os.listdir('json-repos')
    for reponame in list:
        with open('json-repos/' + reponame, "r") as data:
            jsonrepo = json.load(data)
        try:
            jsonPath = ''.join([TREES_DIR,'/',str(jsonrepo['id']),'-',jsonrepo['name'],'.json'])
        except KeyError as error:
            warnMsg = "-------------WARNING---------------\n"
            warnMsg += "Name: " + reponame + '\n'
            warnMsg += "Eror: " + str(error) + '\n'
            warnMsg += "-----------------------------------"
            continue
        url = 'https://api.github.com/repos/{0}/git/trees/{1}?recursive=1'.format(
                                                                            jsonrepo['full_name'],
                                                                            jsonrepo['default_branch'])
        jsontree = getRepoTree(url, jsonPath)
        if not jsontree:
            log("{0}: json tree was downloaded previusly".format(jsonPath), 1)
            continue
        findPythonFiles(jsontree, jsonrepo, reponame)
        sleep(1)

if __name__ == '__main__':
    getPythonFiles()
