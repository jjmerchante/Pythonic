from pythonic import completeAnalysis
import os
import re
import sys
from pymongo import MongoClient
import shutil
import signal


""" Read the main() documentation for defining this variables """

DONE_FOLDER_REPOS = "/home/josejm/python-analysis/code-repos-done"
BIG_FOLDER_REPOS = "/home/josejm/python-analysis/code-repos-big"
MAX_FILES = 1200
FILE_TIMEOUT = 60*5 # 5 minutes
TIMEOUT_LOG = '/home/josejm/python-analysis/errors.txt'
MONGODB_URL = 'mongodb://localhost:27017/'
COLLECTION_NAME = 'idioms'
VERSION_DB = 'v2'



def log(msg, level=0):
    """
    Print a message with differents levels of importance
    0: trace, 1: info, 2: warn, 3: error
    """
    color = ['\033[0m', '\033[94m', '\033[93m', '\033[91m']
    if level < 0  or level > 3: level = 0
    print color[level] + str(msg) + '\033[0m'
    sys.stdout.flush()

def isPythonFile(filepath):
    """
    Is the path passed a Python file?
    """
    isPython = False
    # Commonly files found in repositories and aren't python files
    OMIT_FILES = ['README', 'LICENSE', 'NOTICE', 'HEAD', 'DETAILS', 'BUILD', 'DEPENDS', '.gitignore']
    (root, ext) = os.path.splitext(filepath)
    if root.split('/')[-1] not in OMIT_FILES and not re.search('\/.git\/', root):
        if ext == '.py':
            isPython = True
        elif ext == '':
            with open(filepath, 'r') as file:
                isPython = bool(re.search('#!.*python', file.readline()))
    return isPython


def getPyFilesIn(repo):
    """
    Look for files that aren't written in python language into a repository
    and delete them
    """
    filesList = []
    for root, dirs, files in os.walk(repo):
        for name in files:
            if not re.search('\/.git\/', root):
                filepath = os.path.join(root, name)
                if not os.path.islink(filepath) and isPythonFile(filepath):
                    filesList.append(filepath)
    return filesList


def main(repos):
    """
    - Guiven a list of repositories, analyze each one and store them in a database.
    - If the repository is already analized, will move it to DONE_FOLDER_REPOS.
    - If there are more than MAX_FILES files, doesn't analyze it because could
      overflow the database document limit. Move the repository to BIG_FOLDER_REPOS.
    - Define the maximum time for analyzing one file: FILE_TIMEOUT (0 = disabled).
    - Define the TIMEOUT_LOG for logging when a file analysis wasn't completed.
    - The analysis result will be saved in MONGODB_URL, COLLECTION_NAME, VERSION_DB
    """
    def _handlerTime(sig, frame):
        raise RuntimeError("Excesive time")
    signal.signal(signal.SIGALRM, _handlerTime)

    # Load database
    client = MongoClient(MONGODB_URL)
    db = client[COLLECTION_NAME]

    repostotal = len(repos)
    print "Repositories: " + str(repostotal)
    reposdone = 0
    for repo in repos:
        reponame = repo.split('/')[-1]
        # check if the repository exists in the database
        if db[VERSION_DB].find_one({'repositoryPath': repo}, projection={'_id':True}):
            log(repo + " already analyzed", 2)
            shutil.move(repo, DONE_FOLDER_REPOS)
            reposdone += 1
            continue

        pythonfiles = getPyFilesIn(repo)
        filestotal = float(len(pythonfiles))
        if filestotal > MAX_FILES:
            log("Do this later: " + str(filestotal) + " files", 3)
            shutil.move(repo, BIG_FOLDER_REPOS)
            continue

        filesdone = 0
        documentResult = {
                          "repositoryPath": repo,
                          "idioms": {},
                          "antiidioms": {}
                         }
        for filename in pythonfiles:
            abbrName = reponame + filename.split(repo)[-1]
            porcentage = (reposdone + (filesdone/filestotal))*(float(100)/repostotal)
            print "ANALYZING %s" % filename
            signal.alarm(FILE_TIMEOUT)
            try:
                (results, resultsAnti) = completeAnalysis(filename)
            except RuntimeError as e:
                signal.alarm(0)
                log("******" + str(e) + "******", 3)
                with open(TIMEOUT_LOG, 'a') as timeoutfile:
                    timeoutfile.write(str(e) + ": " + abbrName + "\n")
                continue
            signal.alarm(0)
            for idiom in results:
                if not idiom.name in documentResult['idioms']:
                    documentResult['idioms'][idiom.name] = []
                actualIdiom = documentResult['idioms'][idiom.name]
                for idiomItem in idiom.where:
                    idiomItem['filename'] = abbrName
                    actualIdiom.append(idiomItem)

            for idiomanti in resultsAnti:
                if not idiomanti.name in documentResult['antiidioms']:
                    documentResult['antiidioms'][idiomanti.name] = []
                actualIdiom = documentResult['antiidioms'][idiomanti.name]
                for idiomItem in idiomanti.where:
                    idiomItem['filename'] = abbrName
                    actualIdiom.append(idiomItem)
            filesdone += 1
            print "{0}% completed. {1}/{2} files. {3}/{4} repositories".format(porcentage, filesdone, int(filestotal), reposdone, repostotal)
        db[VERSION_DB].insert(documentResult)
        reposdone += 1

if __name__ == '__main__':
    #os.chdir("/home/josejm/python-analysis/code-repos/")
    if len(sys.argv) == 2:
        os.chdir(sys.argv[1])
        repos = os.listdir(".")
        main(repos)
    else:
        print "usage: python", sys.argv[0], "container_folder"
