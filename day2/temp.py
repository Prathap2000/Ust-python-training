option=int(input('''what you want to do \n 1.c to f \n 2.f to c \n enetr your choice  '''))
if option==1:
    c=int(input(" enter the cel"))
    f=(c * 1.8) + 32
    print("the cel into fer is ",f)
elif option==2:
    f=float(input("enetr the fer"))
    t=(f-32)/1.8
    print("the fer into cel",t)
else:
    print("your choice is invalid")