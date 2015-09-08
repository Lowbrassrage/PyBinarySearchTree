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

    # def __str__(self):
    #     return str(self.leftNode), str(self.value), str(self.rightNode)
    def printMe(self):
        # if node has no children:
        #   print value
        # else:
        #   if node has left:
        #       leftNode.printMe()
        #   if node has right:
        #       rightNode.printMe()
        if self.leftNode is None and self.rightNode is None:
            print(self.value + ' ', end="")
        else:
            if self.leftNode is not None:
                self.leftNode.printMe()
            print(self.value + ' ', end="")
            if self.rightNode is not None:
                self.rightNode.printMe()



def main():
    # nodeList = []
    root = Node('2')
    node7 = Node('7')
    node5 = Node('5')
    node9 = Node('9')
    node25 = Node('25')
    node6 = Node('6')
    node35 = Node('35')
    node11 = Node('11')
    node4 = Node('4')

    # nodeList.append(node1)
    # nodeList.append(node2)
    # nodeList.append(node3)
    # nodeList.append(node4)

    root.setLeft(node7)
    root.setRight(node5)
    node7.setLeft(node25)
    node7.setRight(node6)
    node6.setLeft(node35)
    node6.setRight(node11)
    node5.setRight(node9)
    node9.setLeft(node4)

    # for node in nodeList:
    #     print(node)

    root.printMe()

if __name__ == '__main__':
    main()
