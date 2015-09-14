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

    # def search(self,K):
    #     print(self.value)
    #     if self.value == K:
    #         print('node = to',K)
    #     elif K < self.value :
    #         print('left',K)
    #         if self.leftNode == None:
    #             #self.leftNode.search(K)
    #             print('NONE LEFT')
    #         else:
    #             self.leftNode.search(K)
    #     elif K > self.value :
    #         print('right',K)
    #         if self.rightNode == None:
    #             #self.rightNode.search(K)
    #             print('NONE RIGHT')
    #         else:
    #             self.rightNode.search(K)
    #             #print('NONE RIGHT')






def main():
    # nodeList = []
    root = Node(2)
    node2 = Node(2)
    node7 = Node(7)
    node5 = Node(5)
    node25 = Node(25)
    node6 = Node(6)
    node9 = Node(9)
    node35 = Node(35)
    node11 = Node(11)
    node4 = Node(4)
 


    root.setLeft(node7)
    root.setRight(node5)
    node2.setLeft(node7)
    node2.setRight(node5)
    node7.setLeft(node25)
    node7.setRight(node6)
    node6.setLeft(node35)
    node6.setRight(node11)
    node5.setRight(node9)
    node9.setLeft(node4)
   

    dtree = {
        'node2':node2.value,
        'node2.right':node2.rightNode.value,
        'node2.left':node2.leftNode.value,
        'node7':node7.value,
        'node7.right':node7.rightNode.value,
        'node7.left':node7.leftNode.value,
        'node25':node25.value,
        'node6':node6.value,
        'node6.right':node6.rightNode.value,
        'node6.left':node6.leftNode.value,
        'node35':node35.value,
        'node11':node11.value,
        'node5':node5.value,
        'node5.right':node5.rightNode.value,
        'node9':node9.value,
        'node9.left':node9.leftNode.value,
        'node4':node4.value,
        }

    root.printMe()
    # print('')
    # root.search(20)
    print('')
    print(dtree['node6.right'])



if __name__ == '__main__':
    main()
