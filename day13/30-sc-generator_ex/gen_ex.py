def getnumbers():
    #return list(range(5))

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5





# --------------------------


r = getnumbers()

for i in r:
    print(i)

print("----")

#r = getnumbers()
for i in r:
    print(i)

r = getnumbers()
print(next(r))
print(next(r))
print(next(r))

'''


for i in r:
    print(i)
'''
