# Sample Data
data = [12, 15, 20, 25, 30]

# Step 1: Initialize variables
total_sum = 0
count = 0

# Step 2: Traverse the list manually
for number in data:
    total_sum = total_sum + number
    count = count + 1

# Step 3: Calculate mean
mean_value = total_sum / count

# Step 4: Display result
print("Input Data:", data)
print("Mean:", mean_value)