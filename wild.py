#!/usr/bin/python
import sys
import os
import re

# Constants
path = os.path.expanduser('~/Wildcard/scripts/')
line = os.environ.get("COMP_LINE").split(' ')
line.append('')
if(os.path.isfile(path + line[1]) and os.path.isfile(path + line[1] + '.bash') and line[1] != sys.argv[2]):
        os.execv(path + line[1] + '.bash', [path + line[1], line[1].split("/")[-1], sys.argv[2], sys.argv[3]])

# Args
cur = sys.argv[2]
prev = sys.argv[3]

# Will get up to the last slash and after because it is greedy
match = re.match('(.*)/(.*)', cur)
if (match is None):
    directory = ''
    toComplete = cur
else:
    directory = match.group(1)
    toComplete = match.group(2)

options = os.listdir(path + directory)
newarr = []
for x in options:
    try:
        if(x.index(toComplete) != 0):
            continue
    except (ValueError):
        continue
    tmp = x
    if(not os.path.isfile(os.path.join(path + directory, tmp))):
        tmp += '/'
    # tmp = tmp.replace(toComplete, '', 1)
    print os.path.join(directory, tmp)
    
