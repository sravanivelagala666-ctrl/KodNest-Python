# Read the limit
limit = int(input())

# Initialize the loop variables and total
number = 1
total = 0
# Examine every number from 1 to lomit
while number <= limit:
    if number % 2 == 0:
        total = total + number
    number = number + 1
# Display the result
print(f"Even Sum: {total}")
