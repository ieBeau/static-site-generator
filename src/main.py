from nodes.text_node import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
from nodes.html_node import HTMLNode, LeafNode, ParentNode

from functions.extract import extract_markdown_images, extract_markdown_links
from functions.split import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

def main():
    text = 'This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)'
    print(text_to_textnodes(text))

main()