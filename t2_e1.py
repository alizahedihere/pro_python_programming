def awnser (x,y,z): 
 if z == str("+"): 
 return first_num + second_num 
 if z == str("*"): 
 return first_num * second_num 
 if z == str("/"): 
 return first_num / second_num 
 if z == str("//"): 
 return first_num // second_num 
 if z == str("-"): 
 return first_num - second_num 
 if z == str("**"): 
 return first_num ** second_num 
print("Hello") 
operator = input("Enter Oprator(Supported operators = *,/,-,//,**): ") first_num = int(input("Enter First Number :")) 
second_num = int(input("Enter Second Number :")) print(awnser(first_num,second_num,operator)) 
