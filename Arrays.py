# what is array ?
# an array is a collection of elements of same data type.


# how to create arrays in python ?
# i stands for integer which specifies type of array we are creating.

import array as arr

a = arr.array("i", [1, 2, 3, 4, 5])


# Access array elements (indexes starts from 0 also includes negative indexing)

print(a[2])
# output: 3

print(a[-3])
# output: 3


# Array operations(Arrays are mutables it means they are changeable.)

# 1) find length of array

print(len(a))
# output: 5


# Add element to array

# Methods:

# 1)append() - (add element at the end.)

a.append(6)
print(a)
# output: [1,2,3,4,5,6]


# 2)extend([]) - (add more than one element at the end of an array.)

a.extend([7, 8])
print(a)
# output: [1, 2, 3, 4, 5, 6, 7, 8]


#  3)insert() - (adds element to a specific position in an array)

a.insert(0, 0)
print(a)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Remove elements from array

# Methods -

# 1)pop() - (removes last array element if no parameter passed either removes element from the position parameter and returns it)

a.pop()
print(a)
#  output: [0, 1, 2, 3, 4, 5, 6, 7]

a.pop(-1)
print(a)
#  output: [0, 1, 2, 3, 4, 5, 6]

# 2)remove() - (removes array element of specific value but doesnt return it.)
a.remove(0)
print(a)
# output: [1, 2, 3, 4, 5, 6]


# Array concatenation (all array types must be same.)

b = arr.array("i", [11, 12, 13, 14, 15])
c = arr.array("i")
c = a + b
print(c)
# output: [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]


# Array slicing

print(a[0:2])
# output: [1, 2]

print(a[0:-2])
#  output: [1, 2, 3, 4]

print(c[::-1])
# output:  [15, 14, 13, 12, 11, 6, 5, 4, 3, 2, 1]


# Looping through an array

# 1) for loop
for i in a:
    print(i)
# output:
# 1
# 2
# 3
# 4
# 5
# 6

# 2) While loop
temp = 0
while temp < 5:
    print(a[temp])
    temp += 1
# output:
# 1
# 2
# 3
# 4
# 5
