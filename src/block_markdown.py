import re

def markdown_to_blocks(markdown: str) -> list:
    blocks = []

    parsed_blocks = markdown.split("\n\n")
    for block in parsed_blocks:
        if block == "":
            continue
        blocks.append(block.strip())

    return blocks