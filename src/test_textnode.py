import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_eq_url(self):
        node = TextNode("This is a url node", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a url node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)


    def test_not_eq_url(self):
        node = TextNode("This is a node", TextType.TEXT)
        node2 = TextNode("This is a node", TextType.BOLD)
        self.assertNotEqual(node, node2)


    def test_not_eq_type(self): 
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


    def test_not_eq_url(self):
        node = TextNode("This is a url node", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a url node", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)


    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()