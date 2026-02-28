from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode(text, text_type, url):
    self.text = text
    self.text_type = text_type
    self.text = url

    def __eq__(self, other):
        return True if self is other else NotImplemented

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


