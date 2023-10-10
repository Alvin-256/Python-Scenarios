# Step 1: Create an empty list named beatles
beatles = []

# Step 2: Add John Lennon, Paul McCartney, and George Harrison to the list
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3: Prompt the user to add Stu Sutcliffe and Pete Best to the list using a for loop
for _ in range(2):
    new_member = input("Enter a new member of the band: ")
    beatles.append(new_member)

# Step 4: Remove Stu Sutcliffe and Pete Best from the list
del beatles[3]  # Removes Stu Sutcliffe
del beatles[3]  # Removes Pete Best

# Step 5: Add Ringo Starr to the beginning of the list using the insert() method
beatles.insert(0, "Ringo Starr")

# Print the final list of band members
print("Final list of Beatles members:", beatles)
