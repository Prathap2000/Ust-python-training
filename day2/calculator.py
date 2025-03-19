import math
print(" SIMPLE CALCULATOR")
num1=int(input("enter the num1:"))
op=input('''choice the operation you want to do \n +,-,/,*, mod,sqrt,log \n''')
num2=int(input("enter the num2:"))
if op=="+":
    print("the add of two num is:",num1+num2)
elif op=="-":
    print("the sub of two num is:",num1-num2)
elif op=="*":
    print("the multi of two num is:",num1*num2)
elif op=="/":
    print("the div of two num is :" ,num1/num2)
elif op=="mod":
    print("the mod of two num is:",num1%num2)
elif op=="sqrt":
    print("the sqrt of two num is:",math.sqrt(num1),math.sqrt(num2))
elif op=="log":
    print("the log of two num is:" ,math.log(num1),math.log(num2) )
else:
    print(" choose the operator from the list")