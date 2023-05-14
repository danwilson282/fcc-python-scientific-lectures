#to see methods available
def methods_available():
    t = tuple()
    print(dir(t))
#methods_available()

def sorting():
    d = {'a':10, 'b': 1, 'c':22}
    t = sorted(d.items())
    print(t)
    for k,v in sorted(d.items()):
        print(k,v)

sorting()

def sort_by_value():
    d = {'a':10, 'b': 1, 'c':22}
    tmp = list()
    for k,v in d.items():
        tmp.append((v,k))
    print(tmp)
    tmp = sorted(tmp, reverse=True)
    print(tmp)
    #A better way
    print('Better way...')
    print(sorted( [ (v,k) for k,v in d.items()]))
sort_by_value()

def read_file():
    name = input('Enter File:')
    counts = dict()
    fhand = open(name)
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0)+1
    lst = list()
    for key, val in counts.items():
        newtup = (val,key)
        lst.append(newtup)
    lst = sorted(lst, reverse=True)
    for val, key in lst[:10]:
        print(key,val)
    
    

read_file()
