
#  Taking  input from user
units = float(input("Enter electricity units consumed: "))

#  Initialize bill amount
bill = 0
fixed_charge = 50

#  Apply logic using if elseconditions

if units <= 0:
    bill = 0

elif units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)

elif units <= 500:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

else:
    bill = (100 * 2) + (100 * 3) + (300 * 5) + ((units - 500) * 8)

#  Adding  fixed charge if units > 0
if units > 0:
    bill = bill + fixed_charge

print(f"Total Electricity Bill for {units} units is: ₹{bill}")