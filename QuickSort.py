# Also Called as PARTITION EXCHANGE SORT
# Developed by Tony Hoare in 1959 and published in 1961.
# when implemented well it can be about 2 or 3 times faster than the its main competitors merge and heap sort.
# Divide and conquer based
# THREE RULES
# 1)left <= pivot if true goes to 2nd rule
# 2)left <= pivot if true take next element as left and check with pivot IF false go to 3rd rule
# 3)right>= pivot if true take next value as right and compare if False then swap left and right.

# to get the correct positiion of pivot
def pivotPlace(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quickSort(list1, first, last):
    if first < last:
        p = pivotPlace(list1, first, last)
        print(p)
        quickSort(list1, first, p - 1)
        quickSort(list1, p + 1, last)


list1 = [7, 8, 5, 3, 6, 4, 2]
n = len(list1)
quickSort(list1, 0, n - 1)
print(list1)
