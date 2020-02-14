d = ['push', 'push', 'push', 'push', 'pop', 'pop', 'push', 'push', 'pop', 'push', 'push', 'pop', 'pop', 'pop', 'pop', 'pop']
s = [1,2,3,4,5,6,7,8]
n = []
i = 1
for c in d:
    if c == 'push':
        n.append(i)
        i += 1
    else:
        n.pop()
print(n)