# Merge Sort is a Divide and Conquer algorithm.
# It divides the input array into two halves, calls itself for the two halves,
# and then merges the two sorted halves.


################################## The time complexity of MergeSort is O(n*Log n)
################################## in all the 3 cases (worst, average and best).
def mergeSort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i = 0
        j = 0
        k = 0
        while len(left_list) > i and len(right_list) > j:
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        while len(left_list) > i:
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1
        while len(right_list) > j:
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1


num = int(input("how many numbers you wanna input ?"))
list1 = [int(input()) for x in range(num)]
mergeSort(list1)
print("sorted list is:", list1)
