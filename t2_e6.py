x = int(input("How many number do you enter ?:"))
i = 1 
l = [] 
while i <= x: 
n = int(input(f"Enter Number {i} :")) i += 1 
l.append(n) 
print("------------") 
print(l) 
print("------------") 
l.sort() 
l.reverse() 
h = len(l) 
h -= 1 
print(f"The Biggest Number is : {l[0]}") print("------------") 
print(f"The Smallest Number is : {l[h]}") print("------------")
