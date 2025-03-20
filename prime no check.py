x = int(input("enter a number:"))
if x > 1:
    for i in range(2,int(x**0.5) + 1):
     if x%i==0:
        print(x ,"is not a prime")
        break 
     else:
        print(x,"is a prime")
else:
   print(x,"is not a prime")
       