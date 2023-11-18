# Given lists
number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]

# Function to check if the first and last numbers are the same
def check_first_last_same(numbers):
    return numbers[0] == numbers[-1]

# Check for number_x
result_x = check_first_last_same(number_x)
print(f"For number_x: {result_x}")

# Check for number_y
result_y = check_first_last_same(number_y)
print(f"For number_y: {result_y}")

