import urllib

def getHtml(url):
    """Just an example"""
    assert url, "Cannot get html of None"
    response = urllib.urlopen(url)
    return response.read()

print getHtml('http://localhost')
