from mudule_m import mohit_core 
from mudule_m import hajm_core 
from mudule_m import mohit_zozanagheh 
from mudule_m import masahat_mosalas_ghaem 
print("Hello") 
condition = 'y' 
while condition == 'y': 
 fun = input("Do want to calculate which? (mohit core, hajm core,  mohit zozanagheh, masahat mosalas ghaem) type it :")  if fun == "mohit core": 
 r = int(input("Enter Shoa :")) 
 print("Mohit Core is :",mohit_core(r)) 
 if fun == "hajm core": 
 h = int(input("Enter Shoa :")) 
 print("hajm Core is :", hajm_core(h)) 
 if fun == "mohit zozanagheh": 
 a = int(input("Enter Side 1 :")) 
 b = int(input("Enter Side 2 :")) 
 c = int(input("Enter Side 3 :")) 
 d = int(input("Enter Side 4 :")) 
 print("mohit Zozanagheh :", mohit_zozanagheh(a, b, c, d))  if fun == "masahat mosalas ghaem": 
 o = int(input("Enter Ghaedeh :")) 
 p = int(input("Enter Ertefa :")) 
 print("Masahat Mosalas Ghaem :", masahat_mosalas_ghaem(o,  p)) 
 condition = input("do you want to recalculate (y or n) :") print("Thank You") 
