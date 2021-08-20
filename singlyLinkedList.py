# Node class for creatring node


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Insert operatoins
# at the beginning
# at the end
# between nodes after and before certain node
# class for creating a linked list


class LinkedList:
    def __init__(self):
        self.head = None

    def checkListEmpty(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def addNodeAtBeg(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def addNodeAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def addNodeAfterNode(self, data, x):
        # x for after which position.
        # cant be starting or 1st node
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present...")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def addNodeBeforeNode(self, data, x):
        if self.head is None:
            print("LL is empty...")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref == None:
            print("node not found...")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def addNodeIfEmpty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")

    def deleteNodeFromBegin(self):
        if self.head == None:
            print("LL is empty.")
        else:
            self.head = self.head.ref

    def deleteNodeFromLast(self):
        if self.head == None:
            print("LL is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def deleteAnyNode(self, x):
        if self.head == None:
            print("LL is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present to delete")
        else:
            n.ref = n.ref.ref


LL1 = LinkedList()
LL1.addNodeAtBeg(10)
LL1.addNodeAtEnd(100)
LL1.addNodeAtBeg(11)
LL1.addNodeAtBeg(12)
LL1.addNodeAfterNode(200, 10)
LL1.addNodeBeforeNode(9, 10)
LL1.addNodeBeforeNode(8, 9)
LL1.addNodeIfEmpty(1)
LL1.addNodeAfterNode(13, 11)
LL1.deleteNodeFromBegin()
LL1.deleteNodeFromLast()
LL1.deleteAnyNode(250)
LL1.checkListEmpty()
