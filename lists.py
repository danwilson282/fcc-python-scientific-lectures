a = [1,2,3]
b = [4,5,6]
c=a+b
print(c)
print(c[0:3])
print(c[3:])

#build a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
#check if in list
check = 99 in stuff
print(check)
check = 'cake' in stuff
print(check)