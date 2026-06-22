import random
comp=random.choice([1,2,3])
me=input("what do you wanna choose?\nStone, Paper or Scissor?  ")
mydict={"Stone":1,"Paper":2,"Scissor":3}
reverse={1:"Stone",2:"Paper",3:"Scissor"}
you=mydict[me]
print("computer choosed",reverse[comp],"\nyou choose",reverse[you])

if(comp==1 and you==1):
    print("its a draw😊")
elif(comp==1 and you==2):
    print("congrats you won🥳🥳")
elif(comp==1 and you==3):
    print("You lost...better luck next time😢")
elif(comp==2 and you==1):
    print("You lost...better luck next time😢")
elif(comp==2 and you==2):
    print("its a draw😊")
elif(comp==2 and you==3):
    print("congrats you won🥳🥳")
elif(comp==3 and you==1):
    print("congrats you won🥳🥳")
elif(comp==3 and you==2):
    print("You lost...better luck next time😢")
elif(comp==3 and you==3):
    print("its a draw😊")
else:
    print("The code is wrong....contact developer")   