import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_text_types(self):
        node_plain = TextNode("Plain text", TextType.PLAIN)
        node_bold = TextNode("Plain text", TextType.BOLD)
        self.assertNotEqual(node_plain, node_bold)


if __name__ == "__main__":
    unittest.main()