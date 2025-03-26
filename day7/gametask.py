import random

# function to jumble the word
def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)

# Welcome message
print("\n")
print("Welcome to the WORD JUMBLE GAME")
print("-" * 80)

print("The computer presents a jumbled word")
print("You need to guess it. For every correct guess")
print("you will be offered a point")
print("-" * 80)

# Get the words and process it 
f = open("game.txt")
content = f.read()
f.close()

content = content.split(',')

print("INFO content -> ", content)

Fpoints = 0
Spoints=0

# for every word in list of words
random.shuffle(content)
attemp=0

for word in content:

    print("\n")

    # jumble the word
    jumbled_word = jumble(word)
    print(jumbled_word)
    # ask user input
    user_word = input("Can you guess -> ")

    # show to the computer output


    # compare user input and update points  
    if attemp==0:
        if(user_word == word):
            Fpoints += 2
            print("\U00002705 Correct")
        else:
            points=0
            print("\U00002745 In-correct")
            attemp+=1

    else: #attemp==1:
        if(user_word == word):
            Spoints += 1
            print("\U00002705 Correct")
        else:
            points=0
            print("\U00002745 In-correct")
            attemp+=1
            break
# show the results

print("-" * 80)
print(Fpoints)
print(Spoints)
print(attemp)
if Fpoints + Spoints >=8:
    print("Well done! /n You Got Grade A+")
elif Fpoints + Spoints>=7 or Fpoints + Spoints>=5:
    print("Well done! \n You Got Grade B+")
else:
    print("Need to Improve \n You Got Grade C")

# if(Fpoints > 6):
#     print("You have played well")
# else:
#     print("You need to improve on your vocabulary")