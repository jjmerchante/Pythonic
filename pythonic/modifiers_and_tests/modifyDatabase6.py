# -*- coding: utf-8 -*-
from pymongo import MongoClient

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize

client = MongoClient('mongodb://localhost:27017/')
db = client['idioms']

with open('/home/josejm/a.txt', 'r') as f:
    for line in f:
        print db.v3.remove({'repositoryPath': line.strip()})
