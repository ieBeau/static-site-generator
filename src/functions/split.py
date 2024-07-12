import re
from functions.extract import extract_markdown_images, extract_markdown_links
from nodes.text_node import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_images(text)
        array = re.split(r'!\[.*?\]\(.*?\)', text)
        for index, line in enumerate(array):
            if line == "" and index == 0:
                nodes.append(TextNode(links[index][0], "image", links[index][1]))
            elif line != "":
                nodes.append(TextNode(line, "text"))
                if index < len(links):
                    nodes.append(TextNode(links[index][0], "image", links[index][1]))
        
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        array = re.split(r'\[.*?\]\(.*?\)', text)
        for index, line in enumerate(array):
            if line == "" and index == 0:
                nodes.append(TextNode(links[index][0], "link", links[index][1]))
            elif line != "":
                nodes.append(TextNode(line, "text"))
                if index < len(links):
                    nodes.append(TextNode(links[index][0], "link", links[index][1]))
    
    return nodes

def text_to_textnodes(text):
    node = [TextNode(text, text_type_text)]

    node = split_nodes_image(node)
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, "**", text_type_bold)
    node = split_nodes_delimiter(node, "*", text_type_italic)
    node = split_nodes_delimiter(node, "`", text_type_code)

    return node