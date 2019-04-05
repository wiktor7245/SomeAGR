f = open('keysInsert.txt', 'r')
keysIns = f.read().split(' ')
print(keysIns)
for k in keysIns:
    k = int(k)
print(keysIns)

l = [int(num) for num in keysIns]
print(l)