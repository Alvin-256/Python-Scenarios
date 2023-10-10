# Step 1: Prompt the user to replace the middle number
user_input = int(input("Enter an integer to replace the middle number: "))
numbers = [1, 2, 3, 4, 5]
numbers[2] = user_input

# Step 2: Remove the last element from the list
numbers.pop()

# Step 3: Print the length of the existing list
print("Length of the list:", len(numbers))
