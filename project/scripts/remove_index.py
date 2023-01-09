def remove_index(index_fle_path):
    with open(index_file_path, mode='r') as file:
        content = file.read()
        content = content.split("\n.. toctree:")[0]
        file.close()
    commit_page_changes(index_file_path, content)
    prune_ending_newlines(index_file_path)

