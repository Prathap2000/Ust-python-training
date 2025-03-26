import math

print("Application to find Factorial of n with Exception")
print("_"*80)
#input
userInp=int(input("Enter the number to find factorial:->"))
print("_"*80)
def fact(user):
    if user == 0:
        raise ValueError("Cannot calculate factorial for a negative number🤓🤓")
    elif user <0:
        raise ValueError("Try to enter the +ve number🤓🤓")
    else:
        factn=math.factorial(user)
        print(f"The Factorila of {user} is {factn} 🥳🥳")

try:
    fact(userInp)
except Exception as e:
    print(e)