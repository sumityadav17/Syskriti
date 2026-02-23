
# Step 1: Take user input
number = float(input("Enter a number: "))

# Step 2: Check the number
if (number > 0):
    print(f"Your entered number {number} is positive.")

if (number < 0):

    positive_value = -(number)
    print(f"Your entered number {number} is  negative, however positive value of number is {positive_value}.")

else:
    print(f"Your entered number {number} is zero.")