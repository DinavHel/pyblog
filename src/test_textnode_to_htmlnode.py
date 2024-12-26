import unittest

from textnode import *
from leafnode import LeafNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_invalid_type(self):
        node = TextNode("some text", "invalid type")
        with self.assertRaises(ValueError) as ve:
            text_node_to_html_node(node)
        msg = "invalid text type"
        self.assertEqual(ve.exception.args[0], msg)
    

    def test_text_node(self):
        text = TextNode("raw text", TextType.TEXT)
        html = LeafNode(None, "raw text")
        self.assertEqual(text_node_to_html_node(text), html)


    def test_bold_node(self):
        text = TextNode("bold text", TextType.BOLD)
        html = LeafNode("b", "bold text")
        self.assertEqual(text_node_to_html_node(text), html)


    def test_italic_node(self):
        text = TextNode("italic text", TextType.ITALIC)
        html = LeafNode("i", "italic text")
        self.assertEqual(text_node_to_html_node(text), html)


    def test_code_node(self):
        text = TextNode("code block", TextType.CODE)
        html = LeafNode("code", "code block")
        self.assertEqual(text_node_to_html_node(text), html)
    

    def test_link_node(self):
        text = TextNode("link node", TextType.LINK, "https://boot.dev")
        html = LeafNode("a", "link node", {"href": "https://boot.dev"})
        self.assertEqual(text_node_to_html_node(text), html)


    def test_img_node(self):
        text = TextNode("image alt", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-small.webp")
        html = LeafNode("img", "", {"src": "https://www.boot.dev/img/bootdev-logo-full-small.webp", "alt": "image alt"})
        self.assertEqual(text_node_to_html_node(text), html)