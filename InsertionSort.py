# Insertion Sort is an easy-to-implement, stable sorting algorithm with
# time complexity of O(n²) in the average and worst case, and
#  O(n) in the best case


# For very small n, Insertion Sort is faster than more efficient algorithms such as Quicksort or Merge Sort


def insertionSort(list1):
    for i in range(1, len(list1)):
        current_element = list1[i]
        pos = i
        while current_element < list1[pos - 1] and pos > 0:
            list1[pos] = list1[pos - 1]
            pos = pos - 1
        list1[pos] = current_element
        print(list1, i)


list1 = [2, 7, 5, 9, 6, 3]
insertionSort(list1)
print("sorted list is", list1)
