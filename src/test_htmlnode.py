import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 
    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("div", "Content", props={"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<div class="container" id="main">Content</div>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    if __name__ == "__main__":
        unittest.main()
