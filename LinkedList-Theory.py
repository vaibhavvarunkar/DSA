# what is linked List ?
# A linked list is a linear data structure,
# in which the elements are  stored at different memory locations.
# The elements in a linked list are linked using pointers.


# In simple words, a linked list consists of nodes
# where each node contains a data field and a reference(link) to the next node in the list.

# Types
# Singly Linked List
# Circular Linked List
# Doubly Linked List

# Advantages over arrays
# 1) Dynamic size
# 2) Ease of insertion/deletion


# Drawbacks:
# 1) Random access is not allowed.
#  We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.

# 2) Extra memory space for a pointer is required with each element of the list.

# 3) Not cache friendly. Since array elements are contiguous locations,
#  there is locality of reference which is not there in case of linked lists.


# Doubly linked list

# A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer,
# together with next pointer and data which are there in singly linked list.

# Advantages over singly linked list
# 1) A DLL can be traversed in both forward and backward direction.

# 2) The delete operation in DLL is more efficient if pointer to the node to be deleted is given.

# 3) We can quickly insert a new node before a given node.
# In singly linked list, to delete a node, pointer to the previous node is needed.

# To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using previous pointer.


# Disadvantages over singly linked list
# 1) Every node of DLL Require extra space for an previous pointer.
# It is possible to implement DLL with single pointer though (See this and this).

# 2) All operations require an extra pointer previous to be maintained.
# For example, in insertion, we need to modify previous pointers together with next pointers. For example in following functions for insertions at different positions, we need 1 or 2 extra steps to set previous pointer.


# Circule Linked List

# Circular linked list is a linked list where all nodes are connected to form a circle.There is no NULL at the end.
# A circular linked list can be a singly circular linked list or doubly circular linked list.

# Advantages:
# 1) Any node can be a starting point. We can traverse the whole list by starting from any point.
#  We just need to stop when the first visited node is visited again.


# 2) Useful for implementation of queue. Unlike this implementation,
# we don’t need to maintain two pointers for front and rear if we use circular linked list. We can maintain a pointer to the last inserted node and front can always be obtained as next of last.

# 3) Circular lists are useful in applications to repeatedly go around the list.
# For example, when multiple applications are running on a PC, it is common for the operating system to put the running applications on a list and then to cycle through them, giving each of them a slice of time to execute, and then making them wait while the CPU is given to another application. It is convenient for the operating system to use a circular list so that when it reaches the end of the list it can cycle around to the front of the list.

# 4) Circular Doubly Linked Lists are used for implementation of advanced data structures like Fibonacci Heap.
