import unittest
import sys
from io import StringIO
from Task3 import *


class unitTests(unittest.TestCase):

    """docstring for ClassName"""

    def testSearch(self):
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
        print("setup complete.")

        out = StringIO()
        sys.stdout = out
        root.search(3)
        output = out.getvalue().strip()
        self.assertEqual(output, 'left  3  right  3  node = to  3')

    def testNodeRef2(self):
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
        print("setup complete.")

        out = StringIO()
        sys.stdout = out
        root.search(15)
        output = out.getvalue().strip()
        self.assertEqual(output, 'right  15  left  15  left  15  NONE LEFT')

if __name__ == '__main__':
    unittest.main(exit=False)
