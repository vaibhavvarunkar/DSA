from queue import PriorityQueue

q = PriorityQueue()
strength = 2  # capacity of queue


def func():  # for add operation
    if len(q.queue) == strength:
        print("queue is full can't add...")
    else:
        num = input("enter queue element:")
        num2 = int(input("enter priority of the element:"))
        q.put((num2, num))
        print("element added successfully...")


def show():
    print(q.queue)


def remove():  # removes element depending on priority.
    element = q.get()
    print(f"{element} has been removed...")


def isFull():
    if len(q.queue) == strength:
        print("queue is full.")
    else:
        print("queue is not full...")


while True:
    print(" 1)Add 2) show 3)remove 4)quit 5)isFUll")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        func()
    if ch == 2:
        show()
    if ch == 3:
        remove()
    if ch == 4:
        break
    if ch == 5:
        isFull()
