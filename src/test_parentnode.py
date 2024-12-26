import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_with_leaf_children(self):
        node = ParentNode(tag="p", children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html)


    def test_nested_parents(self):
        nested_parent_1 = ParentNode(tag="p", children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
        ])

        nested_parent_2 = ParentNode(tag="p", children=[
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])

        parent_node = ParentNode(tag="div", children=[nested_parent_1, nested_parent_2])
        html = "<div><p><b>Bold text</b>Normal text</p><p><i>italic text</i>Normal text</p></div>"
        self.assertEqual(parent_node.to_html(), html)

    def test_parent_node_with_no_tag(self):
        node = ParentNode(tag=None, children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        with self.assertRaises(ValueError) as value_error:
            node.to_html()
        error_message = "tag can't be None on ParentNode object"
        self.assertEqual(value_error.exception.args[0], error_message)


    def test_parent_node_with_no_children(self):
        node = ParentNode(tag="p", children=None)
        with self.assertRaises(ValueError) as value_error:
            node.to_html()
        error_message = "children can't be None on ParentNode object"
        self.assertEqual(value_error.exception.args[0], error_message)
