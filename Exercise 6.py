def is_palindrome(number):
    # Convert the number to a string to easily compare it with its reverse
    str_number = str(number)

    # Reverse the string
    reversed_number = str_number[::-1]

    # Compare the original and reversed strings
    return str_number == reversed_number

# Example usage
num = 121

if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
