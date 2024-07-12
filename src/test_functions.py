import unittest

from nodes.text_node import TextNode
from functions.extract import extract_markdown_images, extract_markdown_links
from functions.split import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestTextNode(unittest.TestCase):
    def test_func(self):
        text = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
        print(split_nodes_image([text]))
        # print(extract_markdown_images(text))

        text2 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text")
        print(split_nodes_link([text2]))
        # print(extract_markdown_links(text2))

        text3 = TextNode("This is text with a link [to google](https://www.google.com) and [to no where]", "text")
        print(split_nodes_image([text3]))
        # print(extract_markdown_links(text3))


if __name__ == "__main__":
    unittest.main()