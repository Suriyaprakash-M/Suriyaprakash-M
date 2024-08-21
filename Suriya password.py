import random
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="1234567890"
total=a+b+c
length=int(input("Enter the length of the Password : "))
password="".join(random.sample(total, length))
print("password is : ",password)
