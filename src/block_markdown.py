import re

def markdown_to_blocks(markdown: str) -> list:
    blocks = []

    parsed_blocks = markdown.split("\n\n")
    for block in parsed_blocks:
        if block == "":
            continue
        blocks.append(block.strip())

    return blocks


def block_to_block_type(block: str) -> str:
    heading_pattern = r"#{1,6} "
    heading_match = re.match(heading_pattern, block)
    if heading_match is not None:
        return "heading"
    
    code_pattern = r"\`{3}"
    code_match = re.findall(code_pattern, block)
    if len(code_match) == 2:
        return "code"

    if re.match(r"[(\-,\*) .*]+", block) is not None:
        return "unordered_list"

    quote_pattern = r"[>.*]+"
    if re.match(quote_pattern, block) is not None:
        return "quote"

    if re.match(r"[\d+\. .*]+", block) is not None:
        return "ordered_list"

    return "paragraph"
