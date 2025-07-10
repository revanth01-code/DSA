arr = list(map(int, input("Enter initial array elements: ").split()))
num = int(input("Enter number to insert: "))
arr.append(num)
print("After insertion:", arr)
num = int(input("Enter number to delete: "))
if num in arr:
    arr.remove(num)
    print("After deletion:", arr)
else:
    print("Element not found!")
print("Traversing array:")
for i in arr:
    print(i)
index = int(input("Enter index to update: "))
if 0 <= index < len(arr):
    new_val = int(input("Enter new value: "))
    arr[index] = new_val
    print("After update:", arr)
else:
    print("Invalid index!")
print("Size of array:", len(arr))
