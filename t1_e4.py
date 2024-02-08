def bp(base, power): 
 if base == 0: 
 return 0 
 if power == 1: 
 return base 
 if power == 0: 
 return 1 
 else: 
 return base * bp(base,power-1) 
print("Hello") 
c = 'y' 
while c == 'y': 
 base = int(input("Enter Base Of number :"))  power = int(input("Enter Power of number :"))  print("The Result is :",bp(base,power))  c = input("do you want to recalculate (y or n) :") 
