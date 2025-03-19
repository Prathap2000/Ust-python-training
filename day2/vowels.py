use=input("enetr the text:")
b=use.lower()
v=0
for i in "aeiou":
    v+=b.count(i)
print(v)


