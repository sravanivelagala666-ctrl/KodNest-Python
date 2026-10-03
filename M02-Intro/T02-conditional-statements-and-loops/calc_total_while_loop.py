# Read the value of n
n = int(input())

# Initialize the counter and total
total = 0
count = 1
# Calculate the total using a while loop
while count <= n:
    total = total + count
    count = count + 1
# Display the result
print("Total:", total)
