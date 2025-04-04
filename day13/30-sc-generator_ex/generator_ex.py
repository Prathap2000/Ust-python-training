import random

def getvowels():
    return list('aeiou')

def getvowel2():
    yield 'a'
    yield 'e'
    yield 'i'
    yield 'o'
    yield 'u'

def getdata(n):
    for i in range(n):
        yield random.randint(1, 10)

'''
def getlines(n):
    for i in range(n):
        yield f.readline()
'''

# -------------------------------


data = getvowel2()

for v in data:
    print(v, end=' ')

print(' --- ')

for v in data:
    print(v, end=' ')

print(data)


# ------------------------------

data = getdata(10)
for d in data:
    print(d, end=' ')
print(' ---- ', end=' ')
for d in data:
    print(d, end=' ')
