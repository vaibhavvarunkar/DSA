# Stack is an ordered collection of items where insertion
# and removal of item takes place from same end which is called as top.


# Opposite end is called as base
# It follows LIFO principle.


# operations on stack:
# 1)Push 2) pop 3)peek or top 4) is Empty

# Stack using list

stack = [1, 2, 3]


def push():
    if len(stack) == n:
        print("stack is full...")
    else:
        item = input("enter the element: ")
        stack.append(item)
        print(stack)


def pop():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print(f"removed element is {e}")


def peek():
    if not stack:
        print("stack is empty")
    else:
        e = stack[-1]
        print(f"peek element is {e}")


n = int(input("enter limit of stack:"))


while True:
    print("Select The Operation 1.Push 2.Pop  3.Peek 4. Quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        break
