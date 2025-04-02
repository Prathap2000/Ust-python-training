import random

class game:
    def __init__(self):
    # computer input 
        print("-"*100)
        print("Game Started......")
        print("-"*100)
        self.cmNum=random.randrange(1,100)
        print(self.cmNum)
        self.Attemp=0
        self.userNum=''
    def play(self):
        while self.Attemp<10:
            #user input
            userNum=int(input("Enter the your Guessed number(1-100)-->"))
            if userNum==self.cmNum:
                print("-"*100)
                print("Excellent playing You Won \U00002705")
                print(f"computer guessed number is {userNum}")
                self.Attemp+=1
                print(f"Number of attempts {self.Attemp}/10 ")
                break
            elif userNum>self.cmNum:
                print("-"*100)
                print(f"The guessed number{userNum} is Higher")
                self.Attemp+=1
                print(f"Number of attempts {self.Attemp}/10 ")
            else:
                print("-"*100)
                print(f"The guessed number {userNum} is Lower")
                self.Attemp+=1
                print(f"Number of attempts {self.Attemp}/10 ")
            if self.Attemp==10:
                print("-"*100)
                print("Game Over Bye Bye \U0001F601")

gameP = game()
gameP.play()