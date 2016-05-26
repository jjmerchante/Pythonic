import re #OK
from collections import * #BAD

def foo1(word):
    from os import * #REALLY BAD
    f.open('www')
    return f.read()
