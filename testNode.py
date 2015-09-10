import unittest
import sys
from io import StringIO
from node import *

class unitTests(unittest.TestCase):
    """docstring for ClassName"""

    def testNode1(self):
        root = Node('2')
        node7 = Node('7')
        node5 = Node('5')
        node9 = Node('9')
        node25 = Node('25')
        node6 = Node('6')
        node35 = Node('35')
        node11 = Node('11')
        node4 = Node('4')

        root.setLeft(node7)
        root.setRight(node5)
        node7.setLeft(node25)
        node7.setRight(node6)
        node6.setLeft(node35)
        node6.setRight(node11)
        node5.setRight(node9)
        node9.setLeft(node4)
        print("setup complete.")

        out = StringIO()
        sys.stdout = out
        root.printMe()
        output = out.getvalue().strip()
        self.assertEqual(output, '25 7 35 6 11 2 5 4 9')

    def testNode2(self):
        root = Node('4')

        out = StringIO()
        sys.stdout = out
        root.printMe()
        output = out.getvalue().strip()
        self.assertEqual(output, '4')

if __name__ == '__main__':
    unittest.main(exit=False)
