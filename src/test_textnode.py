import unittest

from nodes.text_node import TextNode
from nodes.alter_node import text_node_to_html_node
from functions.split import text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
    
        text = 'This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)'
        print(text_to_textnodes(text))

        text = 'This is **text** with an *italic* word and a `code block` and a [link](https://boot.dev)'
        print(text_to_textnodes(text))

        text = 'This is **text** with an *italic* word and a '
        print(text_to_textnodes(text))

        # node1 = TextNode("This is a text node", "bold")
        # print(text_node_to_html_node(node1).to_html())

        # node2 = TextNode("This is a text node", "link", "https://")
        # print(text_node_to_html_node(node2).to_html())

        # node3 = TextNode("This is a text node", "italic")
        # print(text_node_to_html_node(node3).to_html())


if __name__ == "__main__":
    unittest.main()