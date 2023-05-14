#like an object in JS
#dict = {}
def simple_dictionary():
    purse = dict()
    purse['money'] = 12
    purse['candy'] = 3
    purse['tissues'] = 75
    print(purse)
#simple_dictionary()

def counting():
    counts = {}
    names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
    #good way
    #for name in names:
    #    if name not in counts:
    #        counts[name] = 1
    #    else:
    #        counts[name] = counts[name]+1
    #better way
    for name in names:
        #get(value, default if not exist)
        counts[name] = counts.get(name,0) +1
    print(counts)
#counting()

def word_histogram():
    counts = dict()
    line=input('Enter a line of text:')
    words = line.split()
    print('Words:', words)
    print('Counting...')
    for word in words:
        counts[word] = counts.get(word,0)+1
    

    for key in counts:
        print(key, counts[key])

    for key,val in counts.items():
        print(key,val)
#word_histogram()

def file_input():
    name = input('Enter File:')
    handle = open(name)
    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0)+1
    bigcount = None
    bigword = None
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
    print(bigword, bigcount)

file_input()