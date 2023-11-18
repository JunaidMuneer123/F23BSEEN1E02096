for i in range(10):
    if i == 0:
        current_number = 0
        previous_number = 0
    else:
        current_number = i
    sum_of_numbers = current_number + previous_number
    print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum_of_numbers}")
    previous_number = current_number
