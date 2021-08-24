# Queue is a linear data structure where element is inserted from one side and removed from another side.

# the end from which items/elements are inserted into queue is called back/rear/tail.

# the end from which the items are removed from is called as front/head.

# it follows FIFO or LILO principle.


# operations in queue
# 1.enqueue
# 2.dequeue
# 3.isFull


queue = []


def enqueue():
    if len(queue) == strength:
        print("cant add queue is full..")
    else:
        item = int(input("enter item to add:"))
        queue.append(item)
        print(queue)


def dequeue():
    if len(queue) == 0:
        print("Queue is empty...")
    else:
        removed = queue.pop(0)
        print(f"removed item is:{removed}")
    print(queue)


def isFull():
    if len(queue) == strength:
        print("Queue is full")
    else:
        print("queue is not full")


strength = int(input("enter queue capacity:"))

while True:
    print("Select Operatoin To Perfrom. 1. Enqueue  2.Dequeue  3.check isFull 4.close")
    ch = int(input())
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        isFull()
    elif ch == 4:
        break
