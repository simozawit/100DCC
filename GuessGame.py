import random
t=True
r=random.randrange(0,100)
x = int (input(" enter a number"))
while(t):
    if(x>r):
       x = int (input(" the number is higher... keep trying..."))
    if(x<r): 
        x = int (input(" the number is smaller... keep trying..."))
    if(x==r):
        print ( " You get it")
        t=False


