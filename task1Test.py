import unittest
import sys
from io import StringIO
from nodeReference import *
from nodeDict import *

class unitTests(unittest.TestCase):
    """docstring for ClassName"""

    def testNodeRef1(self):
        root = nodeReference('2')
        node7 = nodeReference('7')
        node5 = nodeReference('5')
        node9 = nodeReference('9')
        node25 = nodeReference('25')
        node6 = nodeReference('6')
        node35 = nodeReference('35')
        node11 = nodeReference('11')
        node4 = nodeReference('4')

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

    def testNodeRef2(self):
        root = nodeReference('4')

        out = StringIO()
        sys.stdout = out
        root.printMe()
        output = out.getvalue().strip()
        self.assertEqual(output, '4')

    def testNodeDict1(self):

        root = nodeDict()


if __name__ == '__main__':
    unittest.main(exit=False)
