def prime(l): 
global awn 
global aww 
awn = True 
aww = False 
for i in l: 
awn = True 
if i == 1: 
awn = False 
continue 
for z in range(2, i): 
if i % z == 0: 
awn = False 
else: 
continue 
if awn: 
print(i) 
aww = True 
x = int(input("How many number do you enter ?:"))
i = 1 
l = [] 
while i <= x: 
n = int(input(f"Enter Number {i} :")) i += 1 
l.append(n) 
print(l) 
print("Prime Number : ") 
prime(l) 
if aww: 
print("There isn't")
