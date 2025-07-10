r = int(input("Enter number of rows in multidimensional array: "))
c = int(input("Enter number of columns: "))
multi_array = []

for i in range(r):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    multi_array.append(row)

print("Multidimensional Array:")
for row in multi_array:
    print(row)
