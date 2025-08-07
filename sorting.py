import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [64, 34, 25, 5, 22,23,44,233,13,56,78]

list_for_merge = numbers.copy()
list_for_insertion = numbers.copy()

start = time.time()
merge_sort(list_for_merge)
end = time.time()
print("Merge Sort took {:.6f} seconds".format(end - start))
print("Sorted array (Merge Sort):", list_for_merge)

start = time.time()
insertion_sort(list_for_insertion)
end = time.time()
print("Insertion Sort took {:.6f} seconds".format(end - start))
print("Sorted array (Insertion Sort):", list_for_insertion)
