total_bill = float(input("What is the total bill?:"))
percentage_tip = int(input("What % tip would you like to give?:"))
number_of_people = int(input("How many people are splitting the bill?: "))
payment_per_person = (round(float(((percentage_tip / 100 +1) * total_bill) / number_of_people), 2))
print("Each person owes:",payment_per_person)
