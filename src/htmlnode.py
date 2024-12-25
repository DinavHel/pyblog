class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()


    def props_to_html(self) -> str:
        if self.props is None:
            return ''
        html_attr = ''
        for prop in self.props.keys():
            html_attr = f'{html_attr} {prop}="{self.props[prop]}"'
        return html_attr.strip()


    def __repr__(self):
        return f'HTMLNode({self.tag}, "{self.value}", {self.children}, {self.props})'

