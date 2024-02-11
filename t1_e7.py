def end(len_age): 
 i = 0 
 print("--------------------") 
 print("Average and Age ...") 
 while i < len_age: 
 print(f"Student {i+1} (Average : {average[i]} , Age : {age[i]})") 
 i += 1 
def main(): 
 i = 1 
 print("--------------------") 
 print("Start Part 1 !") 
 while True: 
 a = float(input(f"Enter Average of student {i} :")) 
 o = int(input(f"Enter Age of student {i} :")) 
 if i > 7: 
 if a == 0 or o == 0: 
 len_age = len(age) 
 end(len_age) 
 break 
 average.append(a) 
 age.append(o) 
 i += 1 
 print("--------------------") 
age = [] 
average = [] 
main() 
print("End part 1") 
print("--------------------") 
print("Start Part 2 !") 
new_average = average.copy() 
new_average.extend(age) 
print(f"average + age : {new_average}") 
print("End part 2") 
print("--------------------") 
print("Start Part 3 !") 
average.insert(5, 14.25) 
print(f" 14.25 -> 6 : {average}") 
print("End part 3") 
print("--------------------") 
print("Start Part 4 !") 
count_age = int(input("Enter a Number to count in Age :")) 
count_average = float(input("Enter a Number to count in Average :")) 
print(f"({count_average})in average list : ({average.count(count_average)}) and ({count_age}) in age list :  ({age.count(count_age)})") 
print("End part 4") 
print("--------------------")
