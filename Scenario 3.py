
# Define the source list with repetitions
source_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]

# Create a new list to store unique numbers
unique_list = []

# Iterate through the source list
for num in source_list:
    # Check if the number is not already in the unique_list
    if num not in unique_list:
        # If it's not in unique_list, add it
        unique_list.append(num)

# Print the list with repetitions removed
print("List with repetitions removed:", unique_list)

