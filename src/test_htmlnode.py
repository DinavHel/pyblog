import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }

        node = HTMLNode(props=props)
        html_attr = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), html_attr)


    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        anchor = HTMLNode(tag='a', value='Google', props=props)


        node = HTMLNode(tag='p', value="Go to link:", children=[anchor,])
        representation = 'HTMLNode(p, "Go to link:", [HTMLNode(a, "Google", None, {\'href\': \'https://www.google.com\', \'target\': \'_blank\'})], None)'
        self.assertEqual(node.__repr__(), representation)


if __name__ == "__main__":
    unittest.main()
