import re
from pathlib import Path

def label_glossary_terms_in_page(page_path, terms):
    with open(Path(page_path)) as page:
        content = page.read()
        for term in terms:
            if (content.count(term) > 0):
                content = re.sub(f'{term}(?=[.,\s]|$)', f':term:`{term}`', content, count=1)
            if (content.count(term.lower()) > 0):
                content = re.sub(f'{term.lower()}(?=[.,\s]|$)', f':term:`{term.lower()}`', content, count=1)
        page.close()
    return content

