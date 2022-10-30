print("Exercise 1 Data Types\n")
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
# two_digit_number=int(two_digit_number)
first =int(two_digit_number[0])
second = int(two_digit_number[1])
print(first + second)
print()
#PEMDASLR
#()
#**
#*/ //for int
#+-
print("Exercise 2 - BMI Calculator")
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
height = float(height)
weight = int(weight)
bmi = int(weight / (height**2))
print(bmi)
print()
#round()
#score+=1 stead of score = score + 1
#print(f this doesnt req data type change)
print("Exercise 3 - Life in Weeks\n")
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
left = 90 - int(age)
months = (left) * 12
weeks = (left) * 52
days = (left) * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")