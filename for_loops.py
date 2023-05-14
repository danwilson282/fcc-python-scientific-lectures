friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

#If you need the key value
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

#sorting alphabetically
friends.sort()
print(friends)