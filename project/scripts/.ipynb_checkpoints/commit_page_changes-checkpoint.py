from pathlib import Path

def commit_page_changes(page_path, content):
    with open(Path(page_path), "w") as page:
        page.write(content)
        page.close()

