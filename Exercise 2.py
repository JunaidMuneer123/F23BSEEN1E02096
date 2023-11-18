# Get input from the user
user_input = input("Enter a string: ")

# Iterate through the string and print characters at even indices
print("Characters at even indices:")
for index in range(0, len(user_input), 2):
    print(user_input[index])
