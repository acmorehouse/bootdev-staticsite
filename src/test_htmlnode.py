import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html0(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html1(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "another": "property"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" another="property"')

    def test_props_to_html2(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()
