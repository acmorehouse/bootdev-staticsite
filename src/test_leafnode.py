import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
        
    def test_leaf_to_html0(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html1(self):
        node = LeafNode("p", "")
        self.assertNotEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()
