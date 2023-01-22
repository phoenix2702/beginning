def add(x,y):
   return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y 
def div (x,y):
    return x/y
while True:
    option = int(input("Enter Option 1/2/3/4:"))
    X=int(input("Enter 1st number:"))
    Y=int(input("Enter 2nd number:"))
    if option==1:
      print(add(X,Y))  
    if option==2:
      print(sub(X,Y))
    if option==3:
      mul(X,Y)
      print(mul(X,Y))
    if option==4:
      print(div(X,Y)) 
    

   


 



    

