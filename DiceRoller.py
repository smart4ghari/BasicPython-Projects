#Come on you can do this don't lose your hope
import random           #Here we import random module
i="y"
#Conditional statements
while i=="y":
    x = random.randint(1,6) #randint method is used to import random numbers as integers

    if x==1:
        print("-------------")
        print("|           |")
        print("|     O     |")
        print("|           |")
        print("-------------")
    if x==2:
        print("-------------")
        print("| O         |")
        print("|           |")
        print("|         O |")
        print("-------------")
    if x==3:
        print("------------")
        print("|     O     |")
        print("|     O     |")
        print("|     O     |")
        print("-------------")
    if x==4:
        print("-------------")
        print("| O       O |")
        print("|           |")
        print("| O       O |")
        print("------------")
    if x==5:
        print("-------------")
        print("| O       O |")
        print("|     O     |")
        print("| O       O |")
        print("-------------")
    if x==6:
        print("-------------")
        print("| O       O |")
        print("| O       O |")
        print("| O       O |")
        print("-------------")

    i=input("Press y to continue,or press any key to terminate")
