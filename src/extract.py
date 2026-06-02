import re

def extract_markdown_images(self):
    image_matches = re.findall(r"(\!\[.\])(\( \))")
