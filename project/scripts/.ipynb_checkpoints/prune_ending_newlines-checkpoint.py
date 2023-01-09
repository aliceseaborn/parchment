def prune_ending_newlines(page_path):
    with open(page_path, mode='r') as file:
            content = file.read()
            file.close()
    while content[-1] == "\n":
        content = content[0:-1]
    commit_page_changes(page_path, content)

