import re
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text=sections[i], text_type=TextType.TEXT))
            else:
                split_nodes.append(TextNode(text=sections[i], text_type=text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    image_list = []
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for image in images:
        alt = image[(image.find('[') + 1):(image.find(']'))]
        src = image[(image.find('(') + 1):(image.find(')'))]
        image_list.append((alt, src))
    return image_list


def extract_markdown_links(text):
    link_list = []
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for link in links:
        link_list.append(link)
    return link_list
