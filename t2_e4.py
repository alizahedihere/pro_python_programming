def mn(m, n): 
 if m == 0 or m == n: 
 return 1 
 else: 
 return mn(m, n-1) + mn(m-1, n-1) 
def inp(): 
 global m, n 
 n = int(input("Enter First number(n) :"))  m = int(input("Enter Second number(m) :"))  if n < m: 
 print("incorrect Input , Please Write again")  inp() 
 return m 
print("Hello") 
c = 'y' 
while c == 'y': 
 inp() 
 print("The Result is :", mn(m, n)) 
 c = input("do you want to recalculate (y or n) :") 1
