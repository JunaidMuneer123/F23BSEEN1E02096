# Number of rows and columns in the table
rows = 10
columns = 10

# Nested loop to print the multiplication table
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        product = i * j
        print(f"{i} * {j} = {product}\t", end='')
    print()
