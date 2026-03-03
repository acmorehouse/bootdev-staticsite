from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError

        elif self.tag == None or self.tag == '':
            return self.value

        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
