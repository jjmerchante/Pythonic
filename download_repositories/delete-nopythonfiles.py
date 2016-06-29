import os
import re
import time
import sys


def log(msg, level=0):
    """
    Print a message with differents levels of importance
    0: trace, 1: info, 2: warn, 3: error
    """
    color = ['\033[0m', '\033[94m', '\033[93m', '\033[91m']
    if level < 0  or level > 3: level = 0
    print color[level] + msg + '\033[0m'
    sys.stdout.flush()


def isPythonFile(filepath):
    """
    Is the path passed a Python file?
    """
    isPython = False
    # Commonly files found in repositories and aren't python files
    OMIT_FILES = ['README', 'LICENSE', 'NOTICE', 'HEAD', 'DETAILS', 'BUILD', 'DEPENDS', '.gitignore']
    (root, ext) = os.path.splitext(filepath)
    if root.split('/')[-1] not in OMIT_FILES and not re.search('.git', root):
        if ext == '.py':
            isPython = True
        elif ext == '':
            with open(filepath, 'r') as file:
                isPython = bool(re.search('#!.*python', file.readline()))
    return isPython


def deleteNoPyfilesIn(path):
    """
    Look for files that aren't written in python language into a repository
    and delete them
    """
    count = 0
    filesList = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if not re.search('.git', root):
                filepath = os.path.join(root, name)
                if os.path.islink(filepath) or not isPythonFile(filepath):
                    count += 1
                    os.remove(filepath)
                    log("{1}: removed: {0}".format(filepath, count), 1)

    return filesList

if __name__ == '__main__':
    if len(sys.argv) == 2:
        deleteNoPyfilesIn(sys.argv[1])
    else:
        print 'usage: python', sys.argv[0], 'directory'
