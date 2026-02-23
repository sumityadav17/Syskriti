# Sample Data
data = [25, 10, 15, 30, 20]

# Step 1: Find length manually
n = 0
for _ in data:
    n = n + 1

# Step 2: Manual Sorting (Bubble Sort)
for i in range(n - 1):
    for j in range(n - i - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

# Step 3: Calculate Median
if n % 2 == 0:
    middle1 = data[n // 2 - 1]
    middle2 = data[n // 2]
    median_value = (middle1 + middle2) / 2
else:
    median_value = data[n // 2]

# Step 4: Display Results
print("Sorted Data:", data)
print("Median:", median_value)