import unittest

from block_markdown import *


class TestTextNode(unittest.TestCase):

    def test_markdown_to_blocks(self):

        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]

        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)
    

    def test_block_to_header_type(self):
        heading = "# Heading 1"
        expected = "heading"
        actual = block_to_block_type(heading)
        self.assertEqual(expected, actual)

        heading = "## Heading 2"
        expected = "heading"
        actual = block_to_block_type(heading)
        self.assertEqual(expected, actual)

        heading = "### Heading 3"
        expected = "heading"
        actual = block_to_block_type(heading)
        self.assertEqual(expected, actual)

        heading = "#### Heading 4"
        expected = "heading"
        actual = block_to_block_type(heading)
        self.assertEqual(expected, actual)

        heading = "##### Heading 5"
        expected = "heading"
        actual = block_to_block_type(heading)
        self.assertEqual(expected, actual)

        heading = "###### Heading 6"
        expected = "heading"
        actual = block_to_block_type(heading)
        self.assertEqual(expected, actual)
    

    def test_block_to_code_type(self):
        c_code = """```
int main(void)
{
    return 0;
}
```"""
        expected = "code"
        actual = block_to_block_type(c_code)
        self.assertEqual(expected, actual)


    def test_block_to_quote_type(self):
        quote = """> We have to reinvent the wheel every once every once in a while, not because we need a lot of wheels;
> but because we need a lot of inventors.
> -- Bruce Joyce"""
        expected = "quote"
        actual = block_to_block_type(quote)
        self.assertEqual(expected, actual)


    def test_block_to_unordered_list_type(self):
        unordered_list = """* Element 1
* Element 2
- Element 3
- Element 4"""
        expected = "unordered_list"
        actual = block_to_block_type(unordered_list)
        self.assertEqual(expected, actual)


    def test_block_to_ordered_list_type(self):
        unordered_list = """1. Element a
2. Element b
3. Element c
4. Element d"""
        expected = "ordered_list"
        actual = block_to_block_type(unordered_list)
        self.assertEqual(expected, actual)

