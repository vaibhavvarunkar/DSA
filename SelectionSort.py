# Its a simple in place comparison based algorithm.

# using min function

# ###############################       Time Complexity: O(n2)        ########################################


list1 = [1, 4, 6, 9, 2, 3, 8]


# print("Unsorted List is :", list1)


# last value will be sorted automatically that's why length - 1.
for i in range(0, len(list1) - 1):

    # step-1 find min number from the list for each iterration bcoz after 1st loop first element is already sorted.
    min_value1 = min(list1[i:])

    # step2 - find index of the min_value so that we can swap it later.
    # here i is checking the index if list contain repeated values.
    min_index1 = list1.index(min_value1, i)

    # check if the two values are same or different
    if list1[i] != list1[min_index1]:

        # step3 - swap the ith element with the min_value
        list1[i], list1[min_index1] = list1[min_index1], list1[i]


# print("Sorted List is :", list1)

#################################################################################################################################

# With User Input:

list2 = [10, 30, 60, 20, 70, 40, 80, 50]

print("Unsorted List is :", list2)


for i in range(0, len(list2) - 1):
    min_value = list2[i]
    for j in range(i + 1, len(list2)):
        if list2[j] < min_value:  # just chaange this sign for ascending order
            min_value = list2[j]
    min_index = list2.index(min_value, i)
    if list2[i] != list2[min_index]:
        list2[i], list2[min_index] = list2[min_index], list2[i]


print("Sorted List is :", list2)
