from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)
    

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag can't be None on ParentNode object")
        if self.children is None:
            raise ValueError("children can't be None on ParentNode object")
        
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        return html + f"</{self.tag}>"