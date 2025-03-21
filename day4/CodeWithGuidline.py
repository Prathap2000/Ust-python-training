#INPUT
print("Program to find the prime number from given list")
print("_"*80)
print("enter the number (S for stop)")
UserNum=[] #list for storing the user input if its digit
while True:
# getting the input  number from user
    UserInput=input("->")
    if UserInput=="S": # if user enter caps S it will exit from this loop
        break
    if UserInput.isdigit(): # otherwise it will check for digit
        UserNum.append(int(UserInput)) # used typecasting to store the int in the user list 

prime=[] #container to store the prime number
for num in UserNum:
    #chcecking for condition if it give 0 then its not a prime 
    for i in range(2,num):
        if num%i==0:
            break
    else: # else we will append to the prime list or conyainer
        prime.append(num)
print(" the prime in given is ",prime)
