import random

def getrandom(n):
    return [random.randint(1, 100) for i in range(n)]

def getrandom2(n):
    for i in range(n):
        yield random.randint(1, 100)

# ---------------------------------------------------

r1 = getrandom(5)    # List data type
r2 = getrandom2(5)   # generator


print ('\nFirst iteration:')

for i in r1:
    print(i, end=' ')

print('\n------------------------------')

for i in r2:
    print(i, end=' ')

# ------------------------ Python produces generators in several situations such as ...

'''
>>> t1 = ('a', 'b')
>>> t2 = (1, 2)
>>> t3 = zip(t1, t2)
>>> t3
<zip object at 0x00000138F9EBAAC8>
>>> print(t3)
<zip object at 0x00000138F9EBAAC8>
>>> list(t3)
[('a', 1), ('b', 2)]
>>> dict(t3)
{}
>>> list(t3)
[]

>>> t3 = zip(t1, t2)
>>> dict(t3)
{'a': 1, 'b': 2}
>>> dict(t3)
{}
'''





print ('\n\nSecond iteration:')

for i in r1:
    print(i, end=' ')

print('\n------------------------------')

for i in r2:
    print(i, end=' ')


print('\n------------------------------')

r2 = getrandom2(5)   # generator

for i in r2:
    print(i, end=' ')
