from pathlib import Path

def get_terms_from_glossary(glossary_path):
    with open(Path(glossary_path)) as glossary:
        content = glossary.read().splitlines()
        terms = list()
        for line in content:
            term = ""
            if line.count("\t") == 1:
                term = line.replace("\t", "")
                if term != "":
                    terms.append(term)
        glossary.close()
    return terms

