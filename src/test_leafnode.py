import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_node_without_props(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        paragraph = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), paragraph)

    def test_node_with_props(self):
        anchor = "<a href=\"https://www.google.com\">Click me!</a>"
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), anchor)
    

    def test_node_without_tag(self):
        node = LeafNode(tag=None, value="This is some raw test.", props={"irrelevant": "Nodes with no tags do not care about props"})
        raw = "This is some raw test."
        self.assertEqual(node.to_html(), raw)
    

    def test_leaf_node_should_have_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()