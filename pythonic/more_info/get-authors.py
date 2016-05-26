import subprocess
import os
import re

def getAuthorFrom(filepath, line):
    """
    Guiven a file and a line number from a git project, return the author email
    """
    currentDir = os.getcwd()
    FileName = filepath.split('/')[-1]
    FileLocation = '/'.join(filepath.split('/')[:-1])
    try:
        os.chdir(FileLocation)
    except OSError:
        print "Directory not found " + str(FileLocation)

    command = 'git blame -e {0}'.split(' ');
    command.append(FileName)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
    (stdoutdata, stderrdata) = proc.communicate()
    # For a more precise regex obtaining the email:
    # Expected line: 'token (<email@foo.bar>    2016-01-01 20:16:00 +0200  992)  foor = bar ** 2'
    matched = re.search('\w+\s+\(<(.+@.+\..+)>\s+\d+\-\d+\-\d+ \d+\:\d+\:\d+ [\+\-]\d+\s+'+str(line)+'\)', stdoutdata)

    if matched:
        email = matched.groups()[0] # email
    else:
        print "Email not found in {0} line number {1}".format(str(FileName), str(line))
        email = ''

    os.chdir(currentDir)
    return email



print getAuthorFrom('/home/josejm/PYTHON/python-idioms/repositories/bottle/bottls.py', 4076)
