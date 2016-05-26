#!/usr/bin/python3

import pygments
from pygments.lexers import PythonLexer
import sys
from pygments.token import Token
import re
import ast
from collections import defaultdict

if len(sys.argv) != 2:
    sys.exit("Usage: python3 pythonic.py python_file")

with open(sys.argv[1], 'rt') as file:
    code = file.read()

# lexer = PythonLexer()
# lexer.add_filter('tokenmerge')
# tokens = pygments.lex(code, lexer)

# for token in tokens:
#     print token

def log(str):
    print str

def _ignoreStr(str):
    pWhite = re.compile('\s+')
    pQuotes = re.compile('(\')|(\")')
    if pWhite.match(str) or pQuotes.match(str):
        return True
    else:
        return False

def _sameToken(token1, token2):
    return token1[0] is token2[0] and re.match(token2[1], token1[1])

def _findSeqInTokens(sequence, tokens):
    pos = 0

    for ttype, word in tokens:
        print ttype, word
        if _sameToken((ttype, word), sequence[pos]):
            pos += 1
        elif _ignoreStr(word):
            continue
        # Check before start again if it is the first word in the sequence
        elif ttype is sequence[0][0] and re.match(sequence[0][1], word):
            pos = 1
        else:
            pos = 0
        # End?
        if pos >= len(sequence):
            break
    else:
        return False
    return True

def _getIndent(line):
    return len(line) - len(line.lstrip(' '))

def _beginWith(line, ):
    return line.strip().startswith('try')

def basicStructure(code):
    sequence = []
    lexer = PythonLexer()
    lexer.add_filter('tokenmerge')
    tokens = pygments.lex(code, lexer)
    for token in tokens:
        print token

basicStructure(code)
