word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = [first, second, third]

# Slice the string, list and tuple
sliced_word = word[1:-1]
sliced_list = numbers[0:2]
reversed_tuple = record[::-1]

# Display the sliced values
print(f"Sliced Word: {sliced_word}")
print(f"Sliced List: {sliced_list}")
print(f"Reversed Tuple: {reversed_tuple}")
