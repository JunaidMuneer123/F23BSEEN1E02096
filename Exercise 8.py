# Number of rows in the pattern
rows = 5

# Nested loop to print the downward half-pyramid pattern
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end='')
    print()
