rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row:")

for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
    matrix.append(row)

print("Matrix elements:")
for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()

