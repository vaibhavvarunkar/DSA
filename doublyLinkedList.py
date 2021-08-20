# In doubly linked list the node has three parts 1st is reference to prev node 2nd is data and 3rd is reference to next node.
# the prev ref of 1st node and next ref of last node is none.


from typing import NewType


class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def checkListEmpty(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def printLLReverse(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n = n.pref

    def insertWhenEmpty(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def insertAfterNode(self, data, x):
        new_node = Node(data)
        if self.head == None:
            print("LL is empty can't perform  Add after operation..")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not present")
            elif n.nref is None:
                n.nref = new_node
                new_node.pref = n
            else:
                n.nref.pref = new_node
                new_node.nref = n.nref
                n.nref = new_node
                new_node.pref = n

    def insertBeforeNode(self, data, x):
        new_node = Node(data)
        if self.head == None:
            print("LL is empty...")
            return
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("LL is not found")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def deleteNodeAtBeginning(self):
        if self.head is None:
            print("LL is empty")
            return
        else:
            if self.head.nref is None:
                print("LL will be empty after deleting the node.")
            else:
                self.head = self.head.nref
                self.head.pref = None

    def deleteNodeAtEnd(self):
        if self.head is None:
            print("LL is empty")
            return
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x is not present in dll!")


LL1 = DoublyLinkedList()
LL1.insertWhenEmpty(10)
LL1.insertAtBeginning(11)
LL1.insertAtEnd(12)
LL1.insertAtEnd(15)
LL1.insertAfterNode(13, 14)
LL1.insertBeforeNode(9, 11)
LL1.insertBeforeNode(15, 9)
LL1.deleteNodeAtBeginning()
LL1.deleteNodeAtEnd()
LL1.delete_by_value(9)
LL1.checkListEmpty()
