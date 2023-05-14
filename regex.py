import re

def regex_search(x, reg):
    if re.search(reg, x):
        print(x)

def regex_findall(x, reg):
    y = re.findall(reg,x)
    print(y)

name = input('Enter File:')
fhand = open(name)
for line in fhand:
    line = line.rstrip()
    regex = '^Lorem'
    regex_findall(line,regex)

#'\\S+@\\S+' matches email addresses