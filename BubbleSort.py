# Also know as "SINKING SORT".

# It is a simple sorting algorithm which sorts n number of
# elements in the list by comparing the each pair of adjacent
# items and swaps them if they are in wrong order.

# Bubble Sort is an easy-to-implement,
# stable sorting algorithm with a time complexity of O(n²) in the
################         average and worst cases – and O(n) in the best case.       #################################


arr = [1, 3, 2, 5, 4, 7, 6, 100, 300, 60, 40, 1000, 600, 50000, 3000, 750, 890]
for j in range(0, len(arr) - 1):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


print("Sorted array is:", arr)
