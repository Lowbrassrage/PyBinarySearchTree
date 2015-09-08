class Node(object):

    """Node to contain value and date"""
    value = ""
    date = ""
    leftNode = None
    rightNode = None

    def __init__(self, value, date, leftNode=None, rightNode=None):
        self.value = value
        self.date = date
        self.rightNode = rightNode
        self.leftNode = leftNode

    def setLeft(self, left):
        self.leftNode = left

    def setRight(self, right):
        self.rightNode = right

    def __str__(self):
        return str(self.leftNode), str(self.value), str(self.rightNode)


def main():
    # nodeList = []
    root = Node('4', 'July 4 1976')
    nodeA = Node('5', 'July 5 1976')
    nodeI = Node('6', 'July 6 1976')
    nodeJ = Node('7', 'July 7 1976')

    # nodeList.append(node1)
    # nodeList.append(node2)
    # nodeList.append(node3)
    # nodeList.append(node4)

    root.setLeft(nodeA)
    root.setRight(nodeI)
    nodeI.setRight(nodeJ)

    # for node in nodeList:
    #     print(node)

    print(root)

if __name__ == '__main__':
    main()
