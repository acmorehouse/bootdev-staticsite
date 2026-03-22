from textnode.py import TextNode
from htmlnode.py import HTMLNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception('invalid HTML text type')

    match text_node.text_type:
        case TEXT:
            return LeafNode 

