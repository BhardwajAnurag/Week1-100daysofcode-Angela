print("Welcome to Tip Calculator")
print("-------------------------")
bill = float(input("What is the total bill amount\n").replace("$",""))
tip = int(input("How much tip do you wish to give? 10%, 12%, 15%\n").replace("%",""))
tip = tip/100 * bill
#tip is tip/100 then add to bill amount rather go 1.12
people = int(input("How many people to split the bill?\n"))
bill_with_tip = bill + tip
per_person = bill_with_tip / people
print(f"Each person should pay: {per_person:.2f}")