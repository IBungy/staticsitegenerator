import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "greeting"})
        node2 = HTMLNode(tag="div", value="Hello", props={"class": "greeting"})
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "greeting"})
        node2 = HTMLNode(tag="div", value="Hello", props={"class": "farewell"})
        self.assertNotEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "http://example.com", "target": "_blank"})
        expected_html = ' href="http://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)   


    if __name__ == "__main__":
        unittest.main()
