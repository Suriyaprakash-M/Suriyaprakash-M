print("Simple Calculator with Basic Arithmetic Operation")
while True:
   a=int (input("Enter the number 1 :")) 
   b=int (input("Enter the number 2 :")) 
   print("1.add 2.sub 3.multi 4.div")
   c=int(input("choice : ")) 
   if (c==1) :
       print("Addition is : ",a+b)
   elif(c==2) :
       print("Subtraction is : ",a-b)
   elif(c==3) :
       print("Multiplication is : ",a*b)   
   elif(c==4) :
       print("Division is : ",a/b)   
   else:
       print("Invalid input.")
