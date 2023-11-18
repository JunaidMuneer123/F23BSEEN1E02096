# Number of rows in the pattern
rows = 5

# Nested loop to print the pattern
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end='')
    print()
