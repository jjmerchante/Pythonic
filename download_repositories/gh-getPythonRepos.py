"""
This file provides functions for
 - Download the json data of a repository from github
 - Download the full repository
 Beware the getJSON function. It doesn't wait between
 Github API requests and there are restrictions
"""

import csv
import urllib2
import os
import json
import sys
from collections import namedtuple

JSON_DIR = '../../files/json-repos'
REPOS_DIR = '../../files/code-repos'
access_token = ''
#CSV_FILE_REPOS = '../../files/projects_python_2.csv'

ProjectRecord = namedtuple('ProjectRecord', 'id, url, owner_id, name, descriptor, language, created_at, forked_from, deleted, updated_at')

def log(msg, level=0):
    """
    Print a message with differents levels of importance
    0: trace, 1: info, 2: warn, 3: error
    """
    color = ['\033[0m', '\033[94m', '\033[93m', '\033[91m']
    if level < 0  or level > 3: level = 0
    print color[level] + msg + '\033[0m'
    sys.stdout.flush()


def getJSON(urlrepo, filename):
    """
    Download the json of a repository and save it as filename.
    If filename already exists, returns its content, doesn't overwrite it
    """
    if os.path.exists(filename):
        log("{0}: JSON already exists".format(filename), 1)
        with open(filename, 'r') as data:
            jsondata = json.load(data)
        jsondata = ''
    else:
        url = urlrepo + "?access_token=" + access_token
        try:
            response = urllib2.urlopen(url)
            jsondata = json.load(response)
        except urllib2.HTTPError as error:
            jsondata = {}
            warnMsg =  "------------ WARNING -------------\n"
            warnMsg += "url: " + url + '\n'
            warnMsg += "filename: " + filename + '\n'
            warnMsg += "Error: " + str(error) + '\n'
            warnMsg += "----------------------------------"
            log(warnMsg, 2)
        with open(filename, 'w') as fd:
            fd.write(json.dumps(jsondata))
        log("{0}: JSON downloaded and saved".format(filename), 1)
    return jsondata


def downloadRepo(url, dirRepo):
    """
    Download the repository url to the dirRepo directory.
    If there is a directory with the same name as the url
    repository, doesn't download it.
    """
    if not os.path.exists(dirRepo):
        os.mkdir(dirRepo)
    currentDir = os.getcwd()
    os.chdir(dirRepo)
    repoName = url.split('/')[-1][:-4]
    if os.path.exists(repoName):
        log("---WARNING---: {0}: repository already exists".format(dirRepo + repoName), 2)
        #os.chdir(repoName)
        #log({0}: git pull".format(dirRepo + repoName))
        #os.system('git pull')
    else:
        os.system('git clone {0}'.format(url))
        log("{0}: Downloaded repository".format(dirRepo + repoName), 1)
    os.chdir(currentDir)


def getRepositories(fileCSV):
    """
    From a file csv in ghtorrent format, download the json repositories and
    their content from gitub.
    """
    if not os.path.exists(JSON_DIR):
        os.mkdir(JSON_DIR)
    if not os.path.exists(REPOS_DIR):
        os.mkdir(REPOS_DIR)

    with open(fileCSV, "r") as csvinput:
        for contents in csv.reader(csvinput, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\"):
            row = ProjectRecord(*contents)
            jsonPath = JSON_DIR + '/' + str(int(row.id)) + '-' + row.name + '.json'
            jsonData = getJSON(row.url, jsonPath)

            if not jsonData:
                continue

            try:
                cloneURL = jsonData['clone_url']
            except KeyError:
                log("---WARNING---: {0}: clone url not found".format(jsonPath), 2)
                continue
            downloadDir = REPOS_DIR + '/' + str(int(row.id)) + '-' + row.name + '/'
            downloadRepo(cloneURL, downloadDir)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        getRepositories(sys.argv[1])
    else:
        print "Usage: python", sys.argv[0], "csv_file"
