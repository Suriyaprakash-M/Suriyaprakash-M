import random
while True:
    choices=["rock", "paper", "sissor"]
    computer=""
    computer=random.choice (choices) 
    You=input ("Enter your choice:") 
    print(computer)
    if(computer==You) :
        print("draw")
    elif(computer=="rock" and You=="sissor") :
        print("computer win")
    elif(computer=="sissor" and You=="paper") :
        print("computer win") 
    elif(computer=="paper" and You=="rock") :
        print ("computer win") 
    elif(You=="rock" and computer=="sissor") :
        print("you win")
    elif(You=="sissor" and computer=="paper") :
        print("you win") 
    elif(You=="paper" and computer=="rock") :
        print ("you win ")
