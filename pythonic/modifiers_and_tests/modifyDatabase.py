from pymongo import MongoClient
import pythonic as p
import os
import sys

def analyze(filename):
    print "git blame..." + filename
    try:
        (data, err) = p.getGitBlame(filename)
    except OSError:
        return None
    list = [[],[],[]]
    with open(filename, 'rt') as file:
        code = file.read()
        listIdioms = p.findMagicMethods(code)
        print "magic methods found"
        for type in range(len(listIdioms)):
            print len(listIdioms[type].where)
            tot = 0
            for idiomItem in listIdioms[type].where:
                tot+=1
                print str(tot) + '\r',
                sys.stdout.flush()
                idiomItem['filename'] = filename
                if data:
                    idiomItem['author'] = p.getAuthor(data, idiomItem['line'])
                list[type].append(idiomItem)
    return list


if __name__ == '__main__':

    client = MongoClient('mongodb://localhost:27017/')
    db = client['idioms']

    total = 0
    max = db.v2.find().count()
    os.chdir("/home/josejm/python-analysis/code-repos-done/")
    for doc in db.v2.find():
        total += 1
        print "-----" + doc['repositoryPath'] + "--------------"
        files = []
        resTot = [[],[],[]]
        stop = False
        try:
            doc['idioms']['idiomMethods1']
        except:
            with open('/home/josejm/a.txt', 'a') as f:
                f.write(doc['repositoryPath'] + '\n')
            continue
        for idiom in doc['idioms']['idiomMethods1']:
            if 'method' in idiom or stop:
                print "NEXT"
                stop = True
                break
            if not idiom['filename'] in files:
                files.append(idiom['filename'])
                res = analyze(idiom['filename'])
                if res is None:
                    print "WHAT THE HELL IS THIS????????????????????????????????????????????????"
                    print doc
                    raise "Error"
                    stop = True
                    with open('/home/josejm/PYTHON/Pythonista/pythonic/none2.txt', 'a') as f:
                        f.write(doc['repositoryPath'] + "\n")
                else:
                    resTot[0].extend(res[0])
                    resTot[1].extend(res[1])
                    resTot[2].extend(res[2])
        for idiom in doc['idioms']['idiomMethods2']:
            if 'method' in idiom or stop:
                stop = True
                break
            elif not idiom['filename'] in files:
                files.append(idiom['filename'])
                res = analyze(idiom['filename'])
                if res is None:
                    stop = True
                    with open('/home/josejm/PYTHON/Pythonista/pythonic/none.txt', 'a') as f:
                        f.write(doc['repositoryPath'] + "\n")
                else:
                    resTot[0].extend(res[0])
                    resTot[1].extend(res[1])
                    resTot[2].extend(res[2])
        for idiom in doc['idioms']['idiomMethods3']:
            if 'method' in idiom or stop:
                stop = True
                break
            elif not idiom['filename'] in files:
                files.append(idiom['filename'])
                res = analyze(idiom['filename'])
                if res is None:
                    stop = True
                    with open('/home/josejm/PYTHON/Pythonista/pythonic/none.txt', 'a') as f:
                        f.write(doc['repositoryPath'] + "\n")
                else:
                    resTot[0].extend(res[0])
                    resTot[1].extend(res[1])
                    resTot[2].extend(res[2])
        if not stop:
            pass
            """db.v1_1.update_one({'_id': doc['_id']},
                                {
                                    '$set': {'idiomMethods1': resTot[0],
                                             'idiomMethods2': resTot[1],
                                             'idiomMethods3': resTot[2]}
                                })"""

        print str(total) + "/" + str(max)
        print "------------------------------------------------------------------------------------------"
