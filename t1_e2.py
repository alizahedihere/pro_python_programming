def juj(): 
 if first_num > second_num: 
 if first_num > third_num: 
 return first_num 
 else: 
 return third_num 
 if second_num > first_num: 
 if second_num >third_num: 
 return second_num 
 else: 
 return third_num 
 if third_num > second_num: 
 if third_num > first_num: 
 return third_num 
 else: 
 return first_num 
 else: 
 if first_num == second_num: 
 if second_num == third_num: 
 return third_num 
 else: 
 return second_num 
 if first_num == third_num: 
 return first_num 
 if second_num == third_num: 
 return second_num 
first_num = int(input("Enter First number :")) second_num = int(input("Enter Second number :")) third_num = int(input("Enter third number :")) print("The Biggest number is : ",juj()) 
