class Node(object):

    """Node to contain value and date"""
    value = ""
    leftNode = None
    rightNode = None

    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.rightNode = rightNode
        self.leftNode = leftNode

    def setLeft(self, left):
        self.leftNode = left

    def setRight(self, right):
        self.rightNode = right

    def printMe(self):
        # if node has no children:
        if self.leftNode is None and self.rightNode is None:
            # print value
            print(self.value + ' ', end="")
        else:
            # if node has left:
            if self.leftNode is not None:
                self.leftNode.printMe()
            # print value
            print(self.value + ' ', end="")
            # if node has right:
            if self.rightNode is not None:
                self.rightNode.printMe()

class NodeReference(object):

     """Node to contain value and date. Implemented by reference."""
    value = ""
    leftNode = None
    rightNode = None

    def __init__(self, value):
        self.value = value

    def setLeft(self, left):
        self.leftNode = left

    def setRight(self, right):
        self.rightNode = right

    def printMe(self):
        # if node has no children:
        if self.leftNode is None and self.rightNode is None:
            # print value
            print(self.value + ' ', end="")
        else:
            # if node has left:
            if self.leftNode is not None:
                self.leftNode.printMe()
            # print value
            print(self.value + ' ', end="")
            # if node has right:
            if self.rightNode is not None:
                self.rightNode.printMe()

class NodeDict(object):

     """Node to contain value and date. Implemented by reference."""
    value = ""
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def printMe(self):
        # if node has no children:
        if self.leftNode is None and self.rightNode is None:
            # print value
            print(self.value + ' ', end="")
        else:
            # if node has left:
            if self.leftNode is not None:
                self.leftNode.printMe()
            # print value
            print(self.value + ' ', end="")
            # if node has right:
            if self.rightNode is not None:
                self.rightNode.printMe()
