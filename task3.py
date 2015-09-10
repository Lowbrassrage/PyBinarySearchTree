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
            print(self.value , ' ', end="")
        else:
            if self.leftNode is not None:
                self.leftNode.printMe()
            print(self.value , ' ', end="")
            if self.rightNode is not None:
                self.rightNode.printMe()

    def search(self,K):
        print(self.value)
        if self.value == K:
            print('node = to',K)
        elif K < self.value :
            print('left',K)
            if self.leftNode == None:
                #self.leftNode.search(K)
                print('NONE LEFT')
            else:
                self.leftNode.search(K)
        elif K > self.value :
            print('right',K)
            if self.rightNode == None:
                #self.rightNode.search(K)
                print('NONE RIGHT')
            else:
                self.rightNode.search(K)
                #print('NONE RIGHT')




def main():
    # nodeList = []
    root = Node(5)
    node2 = Node(2)
    node21 = Node(21)
    nodeNeg4 = Node(-4)
    node3 = Node(3)
    node19 = Node(19)
    node25 = Node(25)
 


    root.setLeft(node2)
    root.setRight(node21)
    node2.setLeft(nodeNeg4)
    node2.setRight(node3)
    node21.setLeft(node19)
    node21.setRight(node25)


    root.printMe()
    print('')
    root.search(20)


if __name__ == '__main__':
    main()
